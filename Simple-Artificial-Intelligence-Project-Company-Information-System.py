
class Company:
    def __init__(self, company_name, company_budget, personnel_salary, employees):
        self.company_name = company_name
        self.company_budget = company_budget
        self.personnel_salary = personnel_salary
        self.employees = employees

    def list_employees(self):
        return self.employees

    def count_employees(self):
        return len(self.employees)

    def company_info(self):
        return (
            f"Şirket Adı: {self.company_name}\n"
            f"Şirket Bütçesi: {self.company_budget}\n"
            f"Toplam Personel Maaşı: {self.personnel_salary}\n"
            f"Çalışanlar: {', '.join(self.employees)}\n"
            f"Toplam Çalışan Sayısı: {self.count_employees()}"
        )

    def financial_status(self):
        return f"{self.company_name} zararda" if self.company_budget > self.personnel_salary else f"{self.company_name} karda"


def simple_ai_interface(company):
    print("Merhaba, Şirket Bilgi Sistemi'ne hoş geldiniz!")
    print("1 - Şirket Çalışanlarını Listele")
    print("2 - Çalışan Sayısını Göster")
    print("3 - Şirket Bilgilerini Göster")
    print("4 - Şirketin Kar/Zarar Durumunu Göster")
    print("5 - Çıkış")
    while True:
        choice = input("Seçiminiz (1/2/3/4/5): ").strip()
        if choice == "1":
            print("Çalışanlar:", ", ".join(company.list_employees()))
        elif choice == "2":
            print("Toplam Çalışan Sayısı:", company.count_employees())
        elif choice == "3":
            print("Şirket Bilgileri:\n", company.company_info())
        elif choice == "4":
            print("Finansal Durum:", company.financial_status())
        elif choice == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")


def main():
    employees = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]
    company = Company("Örnek Şirket", 100000, 120000, employees)
    simple_ai_interface(company)


if __name__ == "__main__":
    main()
    