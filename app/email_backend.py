import ssl
from django.core.mail.backends.smtp import EmailBackend as DjangoSmtpBackend
from django.utils.functional import cached_property

class SafeEmailBackend(DjangoSmtpBackend): #проблема работ сертификата пайтон 3.13...
    @cached_property
    def ssl_context(self):
        context = ssl.create_default_context()
        
        if hasattr(ssl, 'VERIFY_X509_STRICT'):
            context.verify_flags &= ~ssl.VERIFY_X509_STRICT
            
        return context
