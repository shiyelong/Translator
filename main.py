from flask import Flask, request, jsonify
from googletrans import Translator
import requests
from PIL import Image
from io import BytesIO
import pytesseract
import json

app = Flask(__name__)

# 创建Translator对象
translator = Translator()

# 指定Tesseract-OCR的路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/translate_text', methods=['POST'])
def translate_text():
    data = request.json
    text_to_translate = data.get('text', '')
    dest_language = data.get('dest', 'zh-CN')  # 默认翻译成中文简体
    src_language = data.get('src', 'auto')  # 默认自动检测源语言
    
    # 使用googletrans翻译文本
    translated = translator.translate(text_to_translate, src=src_language, dest=dest_language)
    return jsonify({'translated_text': translated.text.strip()})

@app.route('/translate_images', methods=['POST'])
def translate_images():
    data = request.json
    image_urls = data.get('image_urls', [])
    dest_language = data.get('dest', 'zh-CN')  # 默认翻译成中文简体
    
    translated_texts = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    for url in image_urls:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            
            # 使用pytesseract进行OCR，并指定语言为英语
            ocr_text = pytesseract.image_to_string(image, lang='eng')
            
            if ocr_text:
                # 使用googletrans翻译OCR结果
                translated = translator.translate(ocr_text, src='auto', dest=dest_language)
                translated_texts.append(translated.text.strip())
            else:
                translated_texts.append("无法识别文本")
        except Exception as e:
            translated_texts.append(f"处理图片时出错: {str(e)}")
    
    # 使用json.dumps确保Unicode编码的字符串能够正确转换为明文
    return json.dumps({'translated_texts': translated_texts}, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    app.run(debug=True)
