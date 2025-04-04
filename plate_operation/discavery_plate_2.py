"""
Функція discavery_plate потрібна щоб знайти і витягти номерний знак із фото авто з використанням каскадів Хаара
"""
import cv2

def discavery_plate(car_photo, car_cascade):
    # метод detectMultiScale об'єкта каскаду для виявлення прямокутників, що містять номерні знаки на зображенні.

    # що з себе представляють параметри
    # scaleFactor - наскільки зменшується розмір зображення на кожному етапі масштабування (від 1.0 до 1.5)
    # minNeighbors - скільки сусідніх прямокутників має бути, щоб зберегти об'єкт. 
    # цей параметр допомагає зменшити кількість помилкових спрацьовувань (від 3 до 6)

    gray = cv2.cvtColor(car_photo, cv2.COLOR_BGR2GRAY)

    # Використовуємо каскад Хаара для виявлення номерного знака
    plates = car_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Якщо номерний знак не знайдено, виводимо повідомлення і повертаємо None
    if len(plates) == 0:
        print("Вибачте! Номерні знаки не знайдено.")
        return None

    # Обробляємо перший знайдений номерний знак (якщо їх кілька, беремо перший)
    for (x, y, w, h) in plates:
        cut_number = car_photo[y:y + h, x:x + w]  # Обрізаємо зображення для номерного знака
        return cut_number

    return None