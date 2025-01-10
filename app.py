from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
# Secret key untuk flash messages dan session
app.secret_key = 'fashion_store_secret_key_123'

# Memastikan folder templates ada
if not os.path.exists('templates'):
    os.makedirs('templates')

# Route untuk halaman utama
@app.route('/')
def home():
    # Data produk (bisa diganti dengan database nantinya)
    products = [
        {
            'id': 1,
            'name': 'Kemeja Casual',
            'price': 199000,
            'image': '/api/placeholder/400/300'
        },
        {
            'id': 2,
            'name': 'Dress Modern',
            'price': 299000,
            'image': '/api/placeholder/400/300'
        },
        {
            'id': 3,
            'name': 'Kaos Premium',
            'price': 149000,
            'image': '/api/placeholder/400/300'
        }
    ]
    return render_template('index.html', products=products)

# Route untuk handling form kontak
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Di sini Anda bisa menambahkan logika untuk menyimpan pesan
        # ke database atau mengirim email
        
        # Menambahkan flash message
        flash('Pesan Anda telah terkirim! Kami akan segera menghubungi Anda.', 'success')
        
        return redirect(url_for('home', _anchor='contact'))
    
    # Menjalankan aplikasi dalam mode debug
    app.run(debug=True)