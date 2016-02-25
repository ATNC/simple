1. Настройка системы
  sudo apt-get update
  sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev git
  sudo mysql_install_db
  sudo pip install virtualenv

2. Создание базы и пользователя
  mysql -u root -p
  CREATE DATABASE simple2 CHARACTER SET UTF8;
  CREATE USER simple@localhost IDENTIFIED BY '12345678';
  GRANT ALL PRIVILEGES ON simple2.* TO simple@localhost;
  FLUSH PRIVILEGES;
  exit

3. Скачиваем проект
  git clone https://github.com/ATNC/simple.git

4. Заходим в дирректорию проекта
  cd simple
  virtualenv env
  env/bin/pip install -r requirements.conf
  cd simple/
  ../env/bin/python manage.py migrate

5. Создаем админа
  ../env/bin/python manage.py createsuperuser

6. Запускаем проект
  ../env/bin/python manage.py runserver 0.0.0.0:8000
