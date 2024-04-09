# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>') #method not allowed hatası için burayı int yaptık yaptık
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    try:
        with open("C:/Users/ogn_1/Downloads/Kodland_Müfredat/M3/M3L3/form.txt", "a") as f:
            f.write(f"Isim: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Adres: {address}\n")
            f.write(f"Tarih: {date}\n")
            f.write("-----------------\n")
    except Exception as e:
        print(f"Bir hata aldık => {e}")
    return render_template('form_result.html', name=name, email=email, date = date, address = address)

if __name__ == "__main__":
    app.run(debug=True)


