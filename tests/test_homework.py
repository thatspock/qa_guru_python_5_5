from selene import browser, have, be
import os


def test_homework():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Mr')
    browser.element('#lastName').type('Spock')
    browser.element('#userEmail').type('mrspock@enterprise.com')

    # просто click() почему-то не работает с этой радио кнопкой. только double
    browser.element('#gender-radio-1').should(have.attribute('value', 'Male')).double_click()
    browser.element('#userNumber').type('1800666553')

    browser.element('#dateOfBirthInput').click()
    browser.element('option[value="4"]').click()
    browser.element('option[value="1985"]').click()
    browser.element('div[class*="react-datepicker__day--013"]').should(
        have.attribute('aria-label', 'Choose Monday, May 13th, 1985')).click()

    # Вариант ввода даты через execute_script

    '''
    browser.element('#dateOfBirthInput').click()
    browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
    browser.element('#dateOfBirthInput').send_keys('13 May 1985').press_enter()
    '''

    browser.element('#subjectsInput').type('English').press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()

    # загрузка файла который находится в корне проекта
    browser.element('#uploadPicture').send_keys(os.path.join(os.path.dirname(__file__), 'test.jpg'))

    browser.element('#currentAddress').type('Enterprise (NCC-1701)')

    browser.element('#state #react-select-3-input').type('NCR').press_enter()
    browser.element('#city #react-select-4-input').type('Delhi').press_enter()

    # нажать на кнопку с помощью JavaScript если ее не видно на экране
    browser.execute_script('document.getElementById("submit").click()')

    # Обычный клик
    # browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # проверка всех полей
    browser.all('tbody tr').should(
        have.exact_texts('Student Name Mr Spock', 'Student Email mrspock@enterprise.com', 'Gender Male',
                         'Mobile 1800666553', 'Date of Birth 13 May,1985', 'Subjects English', 'Hobbies Sports',
                         'Picture test.jpg', 'Address Enterprise (NCC-1701)', 'State and City NCR Delhi'))

    browser.element('#closeLargeModal').click()
