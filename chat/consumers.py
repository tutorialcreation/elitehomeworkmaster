import asyncio
import json
from authentication.models import User,Notification
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.core import serializers
from .models import Thread, ChatMessage
from authentication.models import Notification
# from channels import Group

class SupportToWriterConsumer(AsyncConsumer):
        '''
        this is a consumer for facilitating the 
        communication betwen the writers and the client
        '''
        async def websocket_connect(self,event):
            writer=self.scope['url_route']['kwargs']['username']
            support=self.scope['user']
            assignment_id=self.scope['url_route']['kwargs']['pk']
            thread_obj=await self.get_thread(support,writer)
            print(thread_obj)
            self.thread_obj=thread_obj
            # import pdb; pdb.set_trace()
            chat_room=f"thread_{thread_obj.id}"
            self.chat_room=chat_room
            await self.channel_layer.group_add(
                chat_room,
                self.channel_name
            )
            
            await self.send({
                "type":"websocket.accept",
                "text":"hello"
            })


        async def websocket_receive(self,event):
            front_text=event.get('text',None)
            # print(event)
            message_type=event.get('type',None)
            
            if front_text is not None:
                loaded_dict_data=json.loads(front_text)
                msg=loaded_dict_data.get('message')
                notification=loaded_dict_data.get('notification')
                assignment_id=loaded_dict_data.get('assignment_id')
                assignment_creator=loaded_dict_data.get('assignment_creator')
                assignment_support=loaded_dict_data.get('assignment_support')
                assignment_writer=loaded_dict_data.get('assignment_writer')
                payment_status=loaded_dict_data.get('payment_status')
                viewed=loaded_dict_data.get('viewed')
                other_user=self.scope['url_route']['kwargs']['username']
                assignment_id=self.scope['url_route']['kwargs']['pk']
                user=self.scope['user']
                username=user.username
                myResponse={
                    'message':msg,
                    'username':username,
                    'other_user':other_user,
                    'assignment_id':assignment_id,
                    'assignment_creator':assignment_creator,
                    'assignment_support':assignment_support,
                    'assignment_writer':assignment_writer,
                    'payment_status':payment_status,
                    'notification':notification,    
                    'viewed':viewed,
                }
                await self.create_chat_message(user,msg)
                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                        "type":"chat_message",
                        "text":json.dumps(myResponse)
                    }
                )

        async def chat_message(self,event):
            await self.send({
                "type":"websocket.send",
                "text":event['text']
            })

        async def websocket_disconnect(self,close_code):
            await self.channel_layer.group_discard(
                self.chat_room,
                self.channel_name
            )

        @database_sync_to_async
        def get_thread(self,support,writer):
            return Thread.objects.get_or_new(support,writer)[0]

        @database_sync_to_async
        def get_full_thread(self,support,writer):
            return Thread.objects.get_or_new(support,writer)


        @database_sync_to_async
        def create_chat_message(self,me,msg):
            thread_obj=self.thread_obj
            # me=self.scope['user']
            return ChatMessage.objects.create(thread=thread_obj,user=me,message=msg)
        


class SupportToCustomerConsumer(WebsocketConsumer):
    '''
    in this consumer we want to ensure that a customer
    can directly chat with the support team without any issues
    '''
    def fetch_messages(self, data):
        messages = ChatMessage.last_10_messages()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        message = ChatMessage.objects.create(
            user=author_user, 
            message=data['message'])
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.user.username,
            'content': message.message,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name 
        # import pdb;pdb.set_trace()
        self.accept()

    def disconnect(self, close_code):
        print("disconnected") 

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        

    def send_chat_message(self, message):    
        print("send chat message")

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))


class NotificationsConsumer(WebsocketConsumer):
    '''
    this consumer is for basically generating notifications so that
    it may send to the end users who are logged into the system. 
    e.g. 'you have a new message'
    '''
    async def connect(self):
        if  self.scope['user'].is_anonymous:
            await self.close()
        else:
            self.group_name=str(self.scope['user'].pk)
        
    async def disconnect(self,close_code):
            await self.close()
    
    async def notify(self,event):
        self.send(text_data=json.dumps(event['text']))


