# consumers.py in your app directory

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class RideNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'drivers'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        event = {
            'type': 'send_messsage',
            'message': message
        }

        # Send message to WebSocket
        await self.channel_layer.group_send(self.group_name, event)

    async def ridenotification(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    
