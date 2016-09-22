import osmhm

def send_grid_example(from, to, subject, message):
    import sendgrid
    import os

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    data = {
      "personalizations": [
        {
          "to": [
            {
              "email": to
            }
          ],
          "subject": subject
        }
      ],
      "from": {
        "email": from
      },
      "content": [
        {
          "type": "text/plain",
          "value": message
        }
      ]
    }
    response = sg.client.mail.send.post(request_body=data)

osmhm.run(notification=True, notifier=send_grid_example)
