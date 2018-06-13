import eye


code = eye_new.register_password('ahmed', '123456', 'a7medabdeldaim@gmail.com')
# OUTPUT: (401)
print(code)


code, user_name = eye_new.login_password('ahmed', '123456')
# OUTPUT: (501, 'ahmed')
print((code, user_name))


code = eye_new.login('1.jpg')
print(code)
# OUTPUT: (204, '')
