Установка приложения и вход в систему
=====================================

Начало работы
-------------

Программный комплекс состоит из серверной части, веб-интерфейса и мобильных приложений.
Чтобы открыть веб-приложение в браузере, перейдите по |Link| или скопируйте и вставьте ссылку в адресную строку::

    apsk.polyus.com

..  |Link| raw:: html
    
    <a href="http://apsk.polyus.com" target="_blank">ссылке</a>

Мобильные приложения будут предустановлены на ваших устройствах.

..  _login:

Вход в систему
--------------

Пользовательское приложение доступно всем участникам проекта.
В нем осуществляется работа непосредственно с проектом, проектной документацией, замечаниями, предписаниями, отчетами и прочим. 
Для входа в приложение:

*   на персональном компьютере пройдите по ссылке из прошлого пункта,
*   на планшете/смартфоне установите по ссылкам из прошлого пункта приложение «СтройКонтроль» и запустите его.

Если вы входите в приложение через корпоративное мобильное устройство, то вам необходимо ввести полный URL вашей компании::
    
    apsk.polyus.com

..  thumbnail:: images/installing-and-login-0-zero-screen.png
    :alt: Первый экран
    :width: 40%
    :title: Рис. 1. Поле для URL
    :show_caption: True

Дальше инструкция делится на внутренних и внешних сотрудников.

Для внутренних сотрудников
++++++++++++++++++++++++++

Чтобы пользоваться системой внутреннему сотруднику, надо войти в приложение через  **Citrix**. Нажмите на экране в самом низу кнопку Citrix (Рис. 2).

..  thumbnail:: images/installing-and-login-1-first-screen.png
    :alt: Первый экран
    :width: 40%
    :title: Рис. 2. Переход в Citrix
    :show_caption: True

После перехода в **Citrix** вам надо будет выбрать метод двухфакторной аутентификации --- OTP или Certificate.

*   OTP --- это **одноразовый пароль** (`от англ. One Time Password`).
    Этот пароль можно получить в приложении Citrix SSO, Google Authenticator на вашем рабочем устройстве;
*   Certificate --- это файл-ключ, который находится в памяти вашего устройства.
    Как правило, этот файл находится на специальной ключ-флешке. 

    .. note:: Метод входа Certificate недоступен с мобильного устройства.

..  thumbnail:: images/installing-and-login-3-auth-method.png
    :alt: Выбор метода двухфакторной аутентификации
    :width: 40%
    :title: Рис. 3. Выбор метода двухфакторной аутентификации
    :show_caption: True

Выберите метод, который подходит вам и далее вы перейдёте на следующий экран.

..  thumbnail:: images/installing-and-login-4-otp-certificate.png
    :alt: OTP или Certificate
    :width: 70%
    :title: Рис. 4. OTP или Certificate
    :show_caption: True

На примере ниже мы используем для входа OTP. После ввода одноразового пароля нажмите кнопку **Вход**.

..  thumbnail:: images/installing-and-login-5-auth-with-otp.png
    :alt: Вход с помощью OTP
    :width: 70%
    :title: Рис. 5. Вход с помощью OTP
    :show_caption: True

Далее запустится процесс синхронизации и после его завершения вы можете пользоваться приложением.

..  note:: Если вы внутренний сотрудник, то данные для входа автоматически будут вводится на вашем устройстве.
    От вас требуется только пройти двухфакторную аутентификацию.

Для внешних сотрудников
+++++++++++++++++++++++

Для входа внешний сотрудников **Citrix** не требуется. Вы сразу вводите выданные **Email** и **Пароль** в окне ниже. После ввода нажмите кнопку **Sign In**.

..  thumbnail:: images/installing-and-login-6-sign-in-for-aliens.png
    :alt: Вход для внешних сотрудников
    :width: 40%
    :title: Рис. 6. Вход для внешних сотрудников
    :show_caption: True

Далее вам необходимо придумать пароль для своего аккаунта. Дважды введите свой **новый** пароль в поля ниже.

..  thumbnail:: images/installing-and-login-7-pass-update.png
    :alt: Обновление выданного пароля
    :width: 40%
    :title: Рис. 7. Обновление выданного пароля
    :show_caption: True

На следующем окне вас попросят установить на своё мобильное устройство приложение для двухфакторной аутентификации.

Для установки можете найти приложения сами в PlayMarket или AppStore, либо перейти по ссылкам:

* |FreeOTP|
* |Google Authenticator|

..  |FreeOTP| raw:: html
    
    <a href="https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp" target="_blank">FreeOTP</a>

..  |Google Authenticator| raw:: html
    
    <a href="https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp" target="_blank">Google Authenticator</a>

..  thumbnail:: images/installing-and-login-8-auth-setup.png
    :alt: Вход с помощью двухфакторной аутентификации
    :width: 40%
    :title: Рис. 8. Вход с помощью OTP
    :show_caption: True

Для примера мы используем Google Authenticator. После установки и первого запуска приложения нажмите кнопку **Начать**.

..  thumbnail:: images/installing-and-login-9-google-auth-first-screen.png
    :alt: Установка Google Authenticator
    :width: 40%
    :title: Рис. 9. Установка Google Authenticator
    :show_caption: True

Далее нажмите кнопку **Сканировать QR-код** (Рис. 10) и наведите камеру на QR-код из приложения (Рис. 8).

..  thumbnail:: images/installing-and-login-10-google-auth-scan.png
    :alt: Сканирование QR-кода
    :width: 40%
    :title: Рис. 10. Сканирование QR-кода
    :show_caption: True

После этого в поле **One-time code** (Рис. 8) надо будет ввести код, который выдаст Google Authenticator, и нажать кнопку **Submit**.