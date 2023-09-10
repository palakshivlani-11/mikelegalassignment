from Apis.models import Subscriber
import threading
from emailcampaigns.utils import email_template, send_email





def process_email(campaign, subscriber):

    email_content = email_template(campaign, subscriber)
    
    retries = 3  # Number of retries
    while retries > 0:
        try:
            send_email(campaign, subscriber, email_content)
            return  # Email sent successfully, exit the loop
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            retries -= 1



def send_emails(campaign):

    subscribers = Subscriber.objects.filter(subscription_status="active")
    threads = []

    # Create threads for processing emails
    for subscriber in subscribers:
        thread = threading.Thread(
            target=process_email, 
            args=(campaign, subscriber)
        )
        thread.start()
        threads.append(thread)

    # Wait for all the threads to complete
    for thread in threads:
        thread.join()