1. Настройка системы:
  <br>
  sudo apt-get update <br>
  sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev git <br>
  sudo mysql_install_db <br>
  sudo pip install virtualenv <br>

2. Создание базы и пользователя: <br>
  mysql -u root -p <br>
  CREATE DATABASE simple2 CHARACTER SET UTF8; <br>
  CREATE USER simple@localhost IDENTIFIED BY '12345678'; <br>
  GRANT ALL PRIVILEGES ON simple2.* TO simple@localhost; <br>
  FLUSH PRIVILEGES; <br>
  exit <br>

3. Скачиваем проект: <br>
  git clone https://github.com/ATNC/simple.git <br>

4. Заходим в дирректорию проекта: <br>
  cd simple <br>
  virtualenv env <br>
  env/bin/pip install -r requirements.conf <br>
  cd simple/ <br>
  ../env/bin/python manage.py migrate <br>

5. Создаем админа: <br>
  ../env/bin/python manage.py createsuperuser <br>

6. Запускаем проект: <br>
  ../env/bin/python manage.py runserver 0.0.0.0:8000 <br>
