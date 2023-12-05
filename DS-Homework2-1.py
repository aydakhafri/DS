def selection_sort(data):
    n = len(data)

    for i in range(n - 1):
        # پیدا کردن کمترین مقدار باقی‌مانده
        min_index = i
        for j in range(i + 1, n):
            if (data[j]['First Name'] < data[min_index]['First Name'] or
                (data[j]['First Name'] == data[min_index]['First Name'] and data[j]['Last Name'] < data[min_index]['Last Name'])):
                min_index = j

        # جابجایی افراد
        data[i], data[min_index] = data[min_index], data[i]

# داده‌های اولیه
data = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

# اعمال الگوریتم Selection Sort
selection_sort(data)

# نمایش داده‌های مرتب‌شده
print(data)