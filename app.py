from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>หน้าแรก</title></head>
    <body>
        <h1>โย่วเราเห็นเธออ่านข้อความนี้นะ !!</h1>
        เรามีอะไรเล็กๆน้อยๆอยากให้เธออ่ะที่รัก ⸜(｡˃ ᵕ ˂ )⸝♡
        <p><a href="/about">╰┈➤ กดดูตรงนี้สิ </a></p>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <html>
    <head><title>เกี่ยวกับเรา</title></head>
    <body>
        <h1>ลองอ่านดูสิ</h1>
        <p>ไปกันต่ออออ !! </p>
        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓                    
                           
    </body>
    <html>
    <head><title>ติดต่อเรา</title></head>
    <body>
        <h1>อยากอ่านต่อไหม</h1>
        <h1>ʕ´•ᴥ•`ʔ </h1>
        <h1> </h1>
        <h1></h1>
        <p>คัดลอกเเล้วเข้าเว็บนี้สิ</p>
        https://chatgpt.com/share/685f7b19-2aa0-8013-a0b9-4ff11d1dee32
        
    </body>
    </html>
    '''
