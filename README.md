# print_emailed_pdfs
this is used to print a bunch of emailed pdfs from a pop3 account.

I set up my mailbox to filter/only allow email from my/my families email addresses.

This is run via  cron job every 2 minutes.
It connects to the email address, downloads the messages, and if they are from a sender in allowed_senders, and have a .pdf attachment, it prints it.
