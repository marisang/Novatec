import json

from django.test import Client, SimpleTestCase


class ChatViewTests(SimpleTestCase):
    def test_chat_post_accepts_json_request_when_csrf_token_is_sent(self):
        client = Client(enforce_csrf_checks=True)

        page_response = client.get('/')
        csrf_token = page_response.cookies['csrftoken'].value

        response = client.post(
            '/chat/',
            data=json.dumps({'mensagem': 'olá'}),
            content_type='application/json',
            HTTP_X_CSRFTOKEN=csrf_token,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {'resposta': 'Você disse: olá'}
        )
