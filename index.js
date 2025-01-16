// 创建一个基本的HTML页面
document.write(`
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API 使用说明</title>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
        <h1>API 使用说明</h1>
        <h2>主API</h2>
        <p>URL: /api/main</p>
        <p>方法: POST</p>
        <p>示例请求体: {"action": "translate", "text": "你好"}</p>
        <h2>文本翻译API</h2>
        <p>URL: /api/translate</p>
        <p>方法: POST</p>
        <p>示例请求体: {"text": "你好"}</p>
        <h2>图片转文字API</h2>
        <p>URL: /api/imgtotext</p>
        <p>方法: POST</p>
        <p>示例请求体: 文件上传</p>
    </body>
    </html>
    `);
    