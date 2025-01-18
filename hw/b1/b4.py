def main():
    intList = []
    print("nhap so nguuyen (nhap done de ket thuc):")
    while True:
        try:
            intInput = input("Nhap so")
            if intInput.lower() == 'done':
                break
            number = int(intInput)
            intList.append(number)
        except ValueError:
            print("chi nhap so nguyen")
    
    intSum = sum(intList)
    print("Tong:", intSum)

if __name__ == "__main__":
    main()
