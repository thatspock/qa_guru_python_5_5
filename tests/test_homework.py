import time

from selene import browser, have, be


def test_homework():
    browser.open('/')

    browser.element('#firstName').type('Mr')
    browser.element('#lastName').type('Spock')
    browser.element('#userEmail').type('mrspock@enterprise.com')

    # просто click() почему-то не работает с этой радио кнопкой. только double
    browser.element('#gender-radio-1').should(have.attribute('value', 'Male')).double_click()
    browser.element('#userNumber').type('18006665533')

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

    browser.element('#uploadPicture').send_keys('/Users/r/Desktop/test.jpg')

    browser.element('#currentAddress').type('Enterprise (NCC-1701)')

    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    browser.element('#state #react-select-3-input').type('NCR').press_enter()
    browser.element('#city #react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()
