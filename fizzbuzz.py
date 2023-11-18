for i in range(1, 20+1):
    if i % 15==0:   # 15의 배수일 경우 fizzbuzz
        print('fizzbuzz')
    elif i%3==0:    # 3의 배수일 경우 fizz
        print('fizz')
    elif i%5==0:    # 5의 배수일 경우 buzz
        print('buzz')    
    else:
        print(i)