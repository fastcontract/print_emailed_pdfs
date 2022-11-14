# print_emailed_pdfs
this is used to print pdfs that have been sent to my print@asdfasdfadsfa.com pop3 account. 

I set up my mailbox to filter/only allow email from my/my families email addresses.

This then connects to the email address, downloads the messages, and if they are from a sender in allowed_senders, and have a .pdf attachment, it prints it.

This is run via  cron job every 2 minutes.
