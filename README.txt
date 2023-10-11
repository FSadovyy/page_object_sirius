Для запуска автотестов в системе Windows необходимо:

1) Скачать и установить python 3.10: 

	https://www.python.org/downloads/

	Добавить python в PATH

2) Обновить пакетный менеджер pip:
	
	python -m pip install --upgrade pip

3) Установить selenium:

	pip install selenium

4) Скачать и установить webdriver, соответствующую версии тестируемого браузера:

	Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads.
	Firefox: https://github.com/mozilla/geckodriver/releases/ 

	Добавить путь к каждому webdriver в PATH

5) Установить зафиксированные пакеты:
	
	pip install -r requirements.txt

6) Установить плагин pytest-xdist для параллельного запуска тестов:

	pip install pytest-xdist

7) Запустить группу автотестов командой:

		pytest

8) Чтобы изменить параметры запуска, добавить в команду следующие флаги через пробел:

	Запуск в файрфокс:
	
 		--browser_name=firefox

	Запуск х колличества окон (по умолчанию запускается по колличеству тестов):

		-nх

	Метки:
		поставить флаг -m, затем любое колличество меток через пробел

	Запуск только позитивных тест-кейсов:	positive

	Запуск только негативных кейсов:	negative

	Запуск только страничек на английском:	eng

	Запуск только страничек на русском:	ru




	