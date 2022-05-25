def make_url(boldness, font_size, bionic_text):

    html = f"""<!DOCTYPE html>
    <html>
    <meta charset="utf8">
    <title>Bionic Reading Bootleg</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
        bionic {{ color: rgb(0, 0, 0); font-weight:{boldness};font-size:{font_size + 1}px; font-family: Roboto, Georgia; line-height:138%}}
        regular {{ color: rgb(34, 34, 34); font-size: {font_size}px; font-family: Roboto, Georgia; line-height:138%}}
        .column {{
            float: left;
            padding: 10px;
        }}

        .left, .right {{
            width: 30%;
        }}
        .middle {{
            width: 40%;
        }}
        .row:after {{
            content: "";
            display: table;
            clear: both;
        }}


    </style>

    </head>
    <body>
        <div class="row">
            <div class="column left" >
            </div>
            <div class="column middle">
                <p>
                    { bionic_text }
                </p>
            <div class="column right" >
            </div>
            </div>
        </div>
    </body>
    </html>"""

    return html