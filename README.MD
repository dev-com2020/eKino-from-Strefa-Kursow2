--------------------------------------------
DOKUMENTACJA TECHNICZNA DO PROJEKTU "EKINO"

1. Uruchomienie projektu
Aby uruchomić projekt na lokalnym komputerze, należy spłenić nastepujące wymagania związane z bibliotekami:

Python==3.8
dj-database-url==0.5.0
Django==3.0.7
django-allauth==0.41.0
django-crispy-forms==1.9.0
django-debug-toolbar==2.2
Pillow==7.0.0
python-decouple==3.3
sorl-thumbnail==12.6.3
python-decouple==3.3
django-widget-tweaks==1.4.8
django-recaptcha3
django-recaptcha
six

2. Ustawienia procesu rejestracji
Aby proces rejestacji był możliwy, należy w pliku setting.py zmodyfikować sekcję:
# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================
uzupełniając kolejno: 
EMAIL_HOST = "" # wpisz adres serwera pocztowego poczty wychodzącej
EMAIL_PORT = " # podaj numer portu poczty wychodzącej
EMAIL_HOST_USER = "" # podaj login do poczty
EMAIL_HOST_PASSWORD = "" # podaj hasło (możesz je ukryć tak samo, jak przy secret key)
EMAIL_USE_TLS = "" # Protokół zabezpieczenia poczty, wartości True lub False
DEFAULT_FROM_EMAIL = "" # adres który widzi odbiorca wiadomości (nie musi być autentyczny)

ważne: nie stosuj darmowych kont pocztowych (gmail,wp,onet,etc.), są one domyślnie zablokowane do korzystania z tzw. trzecich źródeł. Proces wysyłania wiadomości 
potwierdzających będzie możliwy wyłącznie z domen prywatnych (wystarczy dowolny wykupiony serwer pocztowy z dostępny u wielu providerów).

