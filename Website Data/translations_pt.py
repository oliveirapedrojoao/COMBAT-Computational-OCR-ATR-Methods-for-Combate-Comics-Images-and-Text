# -*- coding: utf-8 -*-
"""translations_pt.py — COMBAT site

Portuguese (European) text of the site. Each key in BLOCKS matches a
data-t="key" element in template.html and holds that element's inner
HTML; the English inner HTML is taken from the template itself at build
time. STRINGS holds the short labels the JavaScript sets at run time.
"""

STRINGS = {
    "en": {
        "nav-home": "Overview", "nav-issues": "Issues", "nav-visuals": "Illustrations",
        "nav-method": "Method", "nav-about": "About",
        "title": "COMBAT — Machine reading of Combate (1974–1978)",
        "all": "All 51", "read": "Read", "save": "Save", "saving": "Saving…", "saved": "Saved",
        "region": "region catalogued", "regions": "regions catalogued",
        "issue": "Issue", "pages": "pages", "pageof": "page {p} of {n}",
        "loading": "Loading page {p}…",
        "loadfail": "This page could not be loaded. Check the internet connection and try again.",
        "back": "← All issues", "savepdf": "Save PDF", "prev": "Previous", "next": "Next",
        "mark": "Mark an illustration", "stopmark": "Stop marking",
        "everything": "Everything", "session": "This session", "sessiontag": "this session",
        "tilemeta": "Issue {i}, page {p}", "preview": "Preview unavailable",
        "prompt": "Name this region (for example: cartoon on the strike)", "untitled": "Untitled region",
        "clipnote": "Marked in the browser; not yet in the catalogue file.",
        "emptyissue": "<h3>No regions catalogued in this issue yet</h3><p style=\"margin:0\">Turn on <em>Mark an illustration</em> above and drag a box over any drawing, photograph or handwritten block.</p>",
        "export": "Export new regions as JSON", "marked": "{n} marked this session",
        "lbmeta": "Issue {i}, page {p}. Box [{b}]. {t}.", "notyet": "Not yet in the catalogue",
        "lbfail": "This region could not be rendered. The PDF may still be downloading, or the connection is off.",
        "lb-png": "Save image", "lb-issue": "Open the issue", "close": "Close",
        "th-label": "First label", "th-box": "Box (x, y, w, h)", "th-dens": "Ink density",
        "extra": "Issue {i}, page {p}: {n} region(s) ({t})",
        "ocrstats": "Tesseract read {w} words on this page with a mean word confidence of {c}%, after the graphic regions were masked. The masked page is {x} × {y} pixels.",
        "types": {"masthead": "masthead", "cartoon": "cartoon", "composed block": "composed block",
                  "handwriting": "handwriting", "photograph": "photograph", "illustration": "illustration",
                  "engraving": "engraving", "unclassified": "unclassified", "drawing": "drawing",
                  "lettering": "lettering"},
    },
    "pt": {
        "nav-home": "Início", "nav-issues": "Números", "nav-visuals": "Ilustrações",
        "nav-method": "Método", "nav-about": "Sobre",
        "title": "COMBAT — Leitura por máquina do Combate (1974–1978)",
        "all": "Todos os 51", "read": "Ler", "save": "Guardar", "saving": "A guardar…", "saved": "Guardado",
        "region": "região catalogada", "regions": "regiões catalogadas",
        "issue": "Número", "pages": "páginas", "pageof": "página {p} de {n}",
        "loading": "A carregar a página {p}…",
        "loadfail": "Não foi possível carregar esta página. Verifique a ligação à internet e tente de novo.",
        "back": "← Todos os números", "savepdf": "Guardar PDF", "prev": "Anterior", "next": "Seguinte",
        "mark": "Marcar uma ilustração", "stopmark": "Parar de marcar",
        "everything": "Tudo", "session": "Esta sessão", "sessiontag": "esta sessão",
        "tilemeta": "Número {i}, página {p}", "preview": "Pré-visualização indisponível",
        "prompt": "Dê um nome a esta região (por exemplo: cartoon sobre a greve)", "untitled": "Região sem título",
        "clipnote": "Marcada no browser; ainda não consta do ficheiro do catálogo.",
        "emptyissue": "<h3>Ainda não há regiões catalogadas neste número</h3><p style=\"margin:0\">Active <em>Marcar uma ilustração</em> acima e arraste uma caixa sobre qualquer desenho, fotografia ou bloco manuscrito.</p>",
        "export": "Exportar as novas regiões em JSON", "marked": "{n} marcada(s) nesta sessão",
        "lbmeta": "Número {i}, página {p}. Caixa [{b}]. {t}.", "notyet": "Ainda não está no catálogo",
        "lbfail": "Não foi possível apresentar esta região. O PDF pode ainda estar a ser descarregado, ou a ligação está desligada.",
        "lb-png": "Guardar imagem", "lb-issue": "Abrir o número", "close": "Fechar",
        "th-label": "Primeira etiqueta", "th-box": "Caixa (x, y, l, a)", "th-dens": "Densidade de tinta",
        "extra": "Número {i}, página {p}: {n} região(ões) ({t})",
        "ocrstats": "O Tesseract leu {w} palavras nesta página com uma confiança média por palavra de {c}%, depois de mascaradas as regiões gráficas. A página mascarada tem {x} × {y} píxeis.",
        "types": {"masthead": "cabeçalho", "cartoon": "cartoon", "composed block": "bloco composto",
                  "handwriting": "manuscrito", "photograph": "fotografia", "illustration": "ilustração",
                  "engraving": "gravura", "unclassified": "por classificar", "drawing": "desenho",
                  "lettering": "letras desenhadas"},
    },
}

REPO = "https://github.com/oliveirapedrojoao/COMBAT-Computational-OCR-ATR-Methods-for-Combate-Comics-Images-and-Text"

BLOCKS = {

"home-hero": """
      <h1>Ler o Combate por máquina</h1>
      <p class="lede">Um jornal operário da revolução portuguesa lido por computador: os desenhos encontrados e catalogados, as colunas convertidas em texto.</p>
      <p class="facts"><b>51 números</b>, <b>487 páginas</b>, <b>de 1974 a 1978</b>. Todas as páginas podem ser lidas aqui, e todos os desenhos que o projecto já catalogou podem ser abertos em plena resolução.</p>
      <div class="actions">
        <a class="btn solid" href="#/issues">Ver os números</a>
        <a class="btn" href="#/method">Como se faz a leitura</a>
      </div>
""",

"home-plate": """
      <img id="hero-img" alt="Página 3 do n.º 1 do Combate com as regiões encontradas pelo detector delineadas a amarelo: um título desenhado à mão, um cabeçalho e um cartoon de dois quadros sobre uma greve antes e depois do 25 de Abril.">
      <figcaption><span class="key"></span>Regiões encontradas automaticamente na página 3 do primeiro número, 21 de Junho de 1974. O cartoon de dois quadros ao fundo da página é todo o editorial.</figcaption>
""",

"home-argument": """
    <h2>Neste jornal, são os desenhos que carregam o argumento</h2>
    <div class="cols">
      <div>
        <p>Na maior parte dos jornais, a ilustração decora o artigo. No <em>Combate</em>, muitas vezes ela <em>é</em> o artigo. Um cartoon de dois quadros faz o trabalho de um editorial; um cartaz de parede fotografado noticia uma greve; uma página escrita à mão é impressa inteira porque veio do chão da fábrica.</p>
        <p>Um processo centrado no texto trata tudo isso como ruído e deita-o fora. Este projecto faz o contrário. Cada desenho, fotografia, gravura, cabeçalho e fac-símile manuscrito é localizado na sua página, recebe um tipo e uma descrição, e fica ligado ao número de onde veio.</p>
      </div>
      <div>
        <p>As digitalizações tornam isto mais difícil do que parece. São cinzentas e de baixo contraste, iluminadas de forma desigual, com a tinta a trespassar do verso da folha, e a paginação não segue nenhum modelo de uma página para a seguinte. As ferramentas correntes falham nelas sem preparação.</p>
        <p>Essa dificuldade é também o que torna o corpus útil. É um caso de teste real e difícil para a leitura por máquina em más condições, e é aberto: as digitalizações, o código e o catálogo estão todos num único repositório público.</p>
        <div class="actions" style="margin-top:10px"><a class="btn" href="#/visuals">Abrir as ilustrações</a></div>
      </div>
    </div>
""",

"issues": """
    <div class="head"><h2>Os 51 números</h2><span class="grey">Transmitidos a partir do repositório do projecto</span></div>
    <p class="wide">Leia qualquer número página a página no browser, ou guarde o PDF. Os números estão agrupados por ano; o primeiro saiu a 21 de Junho de 1974, dois meses depois da revolução.</p>
    <div class="chips" id="yearchips"></div>
    <div class="grid" id="issuegrid"></div>
    <p class="small grey" style="margin-top:26px;max-width:none">A colecção completa está também disponível num único arquivo, com cerca de 143&nbsp;MB.
      <a href="__REPO__/archive/refs/heads/main.zip">Descarregar tudo</a>.</p>
""",

"iv-hint": """Arraste uma caixa à volta de um desenho, fotografia ou bloco manuscrito. Fica no catálogo durante esta sessão e pode ser exportada em JSON a partir da página das ilustrações.""",

"iv-cat": """Catalogado neste número""",

"visuals-intro": """<div class="head"><h2>Ilustrações</h2><span class="grey">Recortadas ao vivo das páginas digitalizadas</span></div>
    <p class="wide">Todas as regiões gráficas catalogadas até agora, recortadas da página em que apareceram. Abra uma para a ver em plena resolução, guardá-la como imagem, ou saltar para o número a que pertence.</p>""",

"galempty": """
      <h3>Ainda nada catalogado com este filtro</h3>
      <p style="margin:0">Abra qualquer número, active <em>Marcar uma ilustração</em> e arraste uma caixa sobre um desenho. Aparecerá aqui durante o resto da sessão.</p>
""",

"method-intro": """<div class="head"><h2>Método</h2><span class="grey">Cinco etapas, do PDF digitalizado a um catálogo</span></div>
    <p class="wide">O projecto lê o <em>Combate</em> com visão por computador clássica e OCR de código aberto, sem redes neuronais treinadas. Tudo o que se segue foi desenvolvido sobre as próprias páginas do jornal, uma etapa de cada vez, e cada etapa vem acompanhada do código que a executa. As três primeiras etapas são automáticas; as duas últimas são primeiro automáticas e depois verificadas à mão.</p>""",

"stagelist": """
      <li><a href="#/method" data-jump="s1"><b>1 Aquisição</b><small>51 PDFs das digitalizações da biblioteca</small></a></li>
      <li><a href="#/method" data-jump="s2"><b>2 Rasterização</b><small>Cada página torna-se um bitmap</small></a></li>
      <li><a href="#/method" data-jump="s3"><b>3 Segmentação da página</b><small>Zonas de texto e zonas gráficas</small></a></li>
      <li><a href="#/method" data-jump="s4"><b>4 Reconhecimento de texto</b><small>As colunas impressas passam por OCR</small></a></li>
      <li><a href="#/method" data-jump="s5"><b>5 Catalogação</b><small>Regiões verificadas e descritas</small></a></li>
""",

"s1": """
      <div class="n">1<small>Aquisição</small></div>
      <div>
        <h2>Reunir o jornal</h2>
        <p>Os 51 números foram reunidos em ficheiros PDF, um por número: 487 páginas no total, entre 2,2 e 8,1&nbsp;MB cada. Os originais em papel estão à guarda da Biblioteca Nacional de Portugal; as cópias digitais aqui usadas foram digitalizadas a partir dessa colecção e postas a circular pelo Marxists Internet Archive, cuja linha de proveniência ainda corre no topo de cada página.</p>
        <p>As digitalizações são a matéria-prima de tudo o que se segue, e são elas que ditam as condições. São a preto e branco, com cerca de 150 píxeis por polegada na maioria dos números, e com uma faixa escura e irregular onde a folha encostou ao vidro do scanner. Nada foi retocado antes do processamento: o método tem de lidar com as páginas tal como estão, porque essa é a condição da maior parte dos jornais digitalizados.</p>
      </div>
""",

"s2": """
      <div class="n">2<small>Rasterização</small></div>
      <div>
        <h2>Transformar cada página num bitmap</h2>
        <p>Uma página de PDF não é uma imagem. É uma lista de instruções: colocar este fluxo de píxeis aqui, traçar esta linha ali. As bibliotecas de visão por computador e de OCR não lêem instruções; lêem grelhas de números. Por isso, a primeira coisa que o método faz é <em>renderizar</em> cada página num <em>bitmap</em>, uma grelha rectangular em que cada célula, um píxel, guarda um valor de cinzento de 0 (tinta preta) a 255 (papel branco).</p>
        <p>A renderização é feita com o <code>pypdfium2</code>, a ligação em Python ao motor de PDF do Chrome. Cada página é desenhada a 150 pontos por polegada, em tons de cinzento, com suavização (<em>anti-aliasing</em>) ligada, e entregue ao <code>OpenCV</code> como uma matriz. A página 3 do n.º 1, por exemplo, mede 1117 × 1582 pontos no PDF e torna-se uma matriz de 3296 linhas por 2328 colunas: 7,7 milhões de números.</p>
        <p>Porquê 150 dpi e não mais? As próprias digitalizações foram feitas aproximadamente a essa resolução, pelo que renderizar mais alto acrescenta píxeis sem acrescentar detalhe, e 487 páginas a 300 dpi levariam quatro vezes mais memória e tempo sem qualquer ganho. A 150 dpi, os contornos mais finos dos cartoons têm ainda dois ou três píxeis de largura, o que chega para a etapa seguinte os seguir.</p>
        <p>A outra coisa que esta etapa fixa é o sistema de coordenadas. Cada caixa que o projecto regista é escrita como fracções da página, de 0 a 1, medidas a partir do canto superior esquerdo, nunca em píxeis. Uma região encontrada num bitmap a 150 dpi pode assim ser recortada de novo a partir de uma renderização a 300 dpi, ou desenhada por este site sobre uma página que o browser renderizou ao tamanho que couber no ecrã. É essa única convenção que permite ao catálogo, ao detector e ao visualizador partilharem os mesmos dados.</p>

        <figure>
          <div class="pix">
            <div>
              <img id="fig-ras-ctx" alt="Pormenor ampliado das letras C e O da palavra COMUNISTA num balão de fala, mostrando os bordos cinzentos e suaves da tinta." style="width:300px;border:1px solid var(--line);background:#fff">
              <img id="fig-ras-patch" alt="Um recorte de 22 por 14 píxeis do mesmo pormenor ampliado catorze vezes, de modo a que cada píxel seja visível." style="width:300px;margin-top:8px;border:1px solid var(--line);image-rendering:pixelated">
            </div>
            <div>
              <table id="pixtable" aria-label="Valores de cinzento das primeiras linhas do recorte ampliado"></table>
              <p class="small grey" style="margin-top:10px;max-width:40ch">As primeiras oito linhas e catorze colunas desse recorte tal como o computador as vê: 0 é preto, 255 é branco. Todas as etapas seguintes são aritmética sobre grelhas como esta.</p>
            </div>
          </div>
          <figcaption>Pormenor do balão de fala do cartoon da página 3 do n.º 1, renderizado a 150 dpi. Os píxeis cinzentos nos bordos são a suavização: o motor de renderização a fazer a média entre tinta e papel onde um traço atravessa a fronteira de um píxel.</figcaption>
        </figure>

        <details class="code">
          <summary>rasterise.py — o código desta etapa</summary>
          <pre id="code-ras"></pre>
          <div class="bar"><button class="btn sm" data-save="rasterise.py">Guardar rasterise.py</button></div>
        </details>
      </div>
""",

"s3": """
      <div class="n">3<small>Segmentação da página</small></div>
      <div>
        <h2>Separar o texto dos desenhos</h2>
        <p>O <em>Combate</em> não tem grelha de página. As colunas mudam de largura de artigo para artigo, os títulos são desenhados à mão, e um cartoon pode estar em qualquer sítio. A comparação com modelos, que funciona em jornais compostos profissionalmente, não tem aqui com que comparar. Por isso, a segmentação não procura uma paginação. Olha para a tinta, e faz a cada marca na página uma única pergunta: isto parece texto corrido, ou não?</p>
        <p>O trabalho faz-se em cinco movimentos, todos com o <code>OpenCV</code>:</p>
        <p><strong>Binarizar.</strong> O bitmap em cinzentos passa a tinta ou papel, sem meio-termo. Como a exposição é desigual, cada píxel é comparado com a média da sua própria vizinhança (uma janela de 51 píxeis) em vez de com um único limiar para toda a página. Assim conserva-se a tinta ténue nos cantos escuros e elimina-se a névoa cinzenta nos claros.</p>
        <p><strong>Remover filetes e margem.</strong> Os filetes de coluna e as molduras são linhas rectas compridas; encontram-se erodindo a tinta com núcleos muito largos e muito altos, e subtraem-se. A faixa escura na borda da digitalização é removida da mesma maneira. Sem este passo, um único filete pode colar um cartoon à coluna ao lado numa só região gigante.</p>
        <p><strong>Mascarar o texto.</strong> O texto corrido é feito de marcas pequenas. Cada mancha de tinta ligada é medida, e qualquer mancha que não seja mais alta do que uma linha de texto, nem demasiado larga, é declarada texto. Os limiares são fracções da altura da página, não contagens de píxeis, pelo que se ajustam a cada digitalização. Um título desenhado à mão falha o teste, e é mantido: é gráfico.</p>
        <p><strong>Agrupar o que resta.</strong> A tinta restante é dilatada para que os traços de um mesmo desenho se toquem, e cada bloco ligado torna-se uma região candidata. Blocos com menos de 0,4% da página, ou mais finos do que um filete de coluna, são descartados. Blocos que se tocam, ou quase, são fundidos, para que as letras separadas de um cabeçalho, ou um desenho e a sua legenda, passem a ser uma só região.</p>
        <p><strong>Classificar.</strong> Cada região recebe uma primeira etiqueta a partir da posição, do tamanho e da densidade de tinta: uma faixa larga no topo da página é um cabeçalho; um bloco escuro e uniformemente preenchido é uma fotografia; uma faixa curta e larga são letras desenhadas; um bloco muito grande é uma página composta; tudo o resto é desenho. Estas etiquetas são um ponto de partida para a etapa 5, não um veredicto.</p>

        <figure>
          <div class="strip">
            <div><img id="fig-seg-grey" alt="Página 3 do n.º 1 tal como renderizada"><span>Página renderizada</span></div>
            <div><img id="fig-seg-ink" alt="A mesma página binarizada: só tinta"><span>Tinta após limiar adaptativo, filetes e margem removidos</span></div>
            <div><img id="fig-seg-text" alt="A máscara de texto: só as marcas pequenas"><span>Máscara de texto: marcas do tamanho de uma linha de texto</span></div>
            <div><img id="fig-seg-rest" alt="Tinta gráfica: o que resta depois de mascarar o texto"><span>Tinta gráfica: o que resta</span></div>
            <div><img id="fig-seg-boxes" alt="A página com as regiões candidatas delineadas"><span>Regiões candidatas após agrupar e fundir</span></div>
          </div>
          <figcaption>Os cinco movimentos sobre a página 3 do n.º 1. O texto corrido desaparece quase por completo no quarto painel, enquanto o título desenhado à mão, os dois cabeçalhos e o cartoon sobrevivem até ao quinto. As regiões encontradas nesta página, com as primeiras etiquetas:</figcaption>
          <table class="regionlist" id="regiontable"></table>
        </figure>

        <h3 style="margin-top:34px">Como se chegou aqui</h3>
        <p style="margin-top:8px">A primeira versão usava um único limiar para toda a página e uma dilatação grande, e em quase todas as páginas devolvia uma só região: a folha inteira. Duas coisas causavam isso. A margem escura da digitalização tocava em tudo, e a dilatação juntava as colunas de texto aos desenhos entre elas. Remover a margem e os filetes resolveu a primeira; a segunda exigiu outra ideia do que é texto.</p>
        <p>Uma primeira máscara de texto tentava encontrar <em>linhas</em> de texto juntando os glifos na horizontal. Funcionava em colunas limpas e falhava sempre que as linhas estavam muito apertadas ou a digitalização estava esborratada, o que no <em>Combate</em> acontece muitas vezes. Medir as marcas uma a uma, e chamar texto às marcas pequenas, revelou-se mais robusto, porque não depende de as linhas serem separáveis. A última alteração foi exprimir todos os limiares de tamanho como fracções da página, já que o n.º 25 é uma dupla página horizontal com 3744 píxeis de largura e o n.º 20 tem 1378; a mesma contagem de píxeis significa coisas diferentes em cada um.</p>
        <p>Mais três páginas, corridas com os parâmetros finais:</p>
        <div class="gal3" id="seg-extra"></div>

        <details class="code">
          <summary>segment.py — o código desta etapa</summary>
          <pre id="code-seg"></pre>
          <div class="bar"><button class="btn sm" data-save="segment.py">Guardar segment.py</button></div>
        </details>
      </div>
""",

"s4": """
      <div class="n">4<small>Reconhecimento de texto</small></div>
      <div>
        <h2>Ler as colunas impressas</h2>
        <p>Conhecidas as regiões gráficas, o texto impresso pode ser lido sem que elas atrapalhem. O motor é o <code>Tesseract</code> com o seu modelo de português, chamado a partir de Python através do <code>pytesseract</code>. Mas o Tesseract corrido directamente sobre uma digitalização em bruto do <em>Combate</em> produz pouco de útil, por isso a página é preparada primeiro, em quatro passos.</p>
        <p><strong>Endireitar.</strong> A inclinação da tinta é medida na página binarizada e o bitmap é rodado de volta à horizontal. Uma digitalização de um jornal dobrado raramente está direita, e mesmo um grau de inclinação custa ao Tesseract palavras inteiras no fim das linhas.</p>
        <p><strong>Limpar e nivelar.</strong> O grão do scanner é removido com um filtro de médias não locais. Depois, o tom local do papel é estimado com um desfoque de mediana largo e a página é dividida por ele, o que nivela a exposição: tinta cinzenta em papel cinzento num canto e tinta preta em papel branco noutro passam a ser a mesma coisa em todo o lado.</p>
        <p><strong>Esticar o contraste.</strong> A equalização adaptativa de histograma (CLAHE) acentua a diferença entre tinta e papel, bloco a bloco, sem rebentar as partes que já estavam nítidas.</p>
        <p><strong>Mascarar os gráficos.</strong> Cada região da etapa 3 é pintada de branco. É por isso que a segmentação vem primeiro: uma legenda escrita dentro de um cartoon, ou o lema num cartaz, seria de outro modo lida como uma linha perdida do artigo ao lado e iria parar ao parágrafo errado.</p>
        <p>A página preparada passa então pelo Tesseract em modo de segmentação automática (<code>--psm 3</code>), que deixa o motor encontrar as colunas por si; não há grelha para lhe dar. O resultado é o texto e, para cada palavra, um valor de confiança, que o projecto guarda para que as passagens fracas possam ser encontradas e verificadas mais tarde.</p>

        <figure>
          <div class="two">
            <div><img id="fig-ocr-raw" alt="Primeira coluna da página 3 do n.º 1 tal como digitalizada: cinzenta, de baixo contraste"><span>A primeira coluna da página 3, n.º 1, tal como digitalizada</span></div>
            <div><img id="fig-ocr-clean" alt="A mesma coluna depois de endireitada, limpa, nivelada e com o contraste esticado: tipo preto sobre branco"><span>A mesma coluna depois da preparação</span></div>
          </div>
          <div class="ocrout">
            <div>
              <h4>O que o Tesseract devolve para essa coluna</h4>
              <pre class="paper" id="ocr-sample" style="margin-top:8px"></pre>
            </div>
            <div>
              <h4>Página inteira</h4>
              <p class="small" style="margin-top:8px" id="ocr-stats"></p>
              <p class="small">As quebras de linha com hífen ficam tal como estão na página. Juntá-las, e corrigir os erros residuais contra um léxico de português, é uma passagem separada.</p>
            </div>
          </div>
          <figcaption>Reconhecimento numa das páginas mais limpas da colecção. Nos números esborratados de 1975 e 1976 a confiança cai a pique, e essas páginas são a razão por que a preparação importa mais do que a escolha do motor.</figcaption>
        </figure>

        <div class="callout">
          <p><strong>Manuscrito não é OCR.</strong> O <em>Combate</em> imprimiu fac-símiles de comunicados, cartas e cartazes escritos à mão, e são em número suficiente para que ignorá-los distorcesse o registo. São encontrados pela etapa 3 e postos de lado aqui, porque um motor de texto impresso devolve disparates sobre eles. São objecto de um esforço separado de reconhecimento de texto manuscrito (HTR), que precisa de um modelo treinado no próprio corpus.</p>
        </div>

        <details class="code">
          <summary>ocr.py — o código desta etapa</summary>
          <pre id="code-ocr"></pre>
          <div class="bar"><button class="btn sm" data-save="ocr.py">Guardar ocr.py</button></div>
        </details>
      </div>
""",

"s5": """
      <div class="n">5<small>Catalogação</small></div>
      <div>
        <h2>Verificar e descrever os gráficos</h2>
        <p>A etapa 3 encontra candidatas; não sabe o que significam. O catálogo é a camada em que uma pessoa olha para cada região contra a sua página, mantém ou corrige a caixa, dá-lhe um tipo de uma lista fixa, e escreve um título e uma nota a dizer o que mostra. É daí que a página das ilustrações deste site lê.</p>
        <p>A verificação faz-se no visualizador de números deste site. Qualquer página pode ser aberta, <em>Marcar uma ilustração</em> activado, e uma caixa arrastada sobre um desenho; a caixa é guardada nas mesmas coordenadas relativas à página que o detector produz, e pode ser exportada em JSON para ser acrescentada ao ficheiro do catálogo no repositório. Um registo por região:</p>
<pre>{
  "issue": 20,                       // número do jornal, 1 a 51
  "page": 5,                         // página dentro do PDF do número
  "box": [0.05, 0.50, 0.36, 0.205],  // x, y, largura, altura, 0 a 1
  "type": "illustration",            // cartoon · photograph · engraving ·
                                     // handwriting · masthead · composed block
  "title": "So juntos venceremos",
  "note": "Cabeçalho do boletim da comissão de moradores de Massarelos."
}</pre>
        <p>Nada neste site guarda uma imagem de uma região. Cada uma é recortada ao vivo do PDF, na resolução de que o ecrã precisa, usando apenas estes seis campos. Se uma caixa for corrigida no catálogo, todas as vistas dela mudam de uma vez.</p>
      </div>
""",

"s6": """
      <div class="n" style="color:var(--ink);font-size:2rem;line-height:1.1">Porque importa</div>
      <div>
        <p>Os jornais digitalizados tornam-se normalmente pesquisáveis correndo OCR e descartando tudo o que não é texto. Num jornal como o <em>Combate</em>, isso descarta o argumento: os cartoons, os panfletos reproduzidos, as páginas manuscritas que foram impressas precisamente por serem manuscritas. Tratar as regiões gráficas como fontes primárias, com coordenadas e descrições, devolve esse material ao alcance dos historiadores, e fá-lo para uma colecção inteira e não para meia dúzia de imagens célebres.</p>
        <p>O método é também deliberadamente simples. Limiares adaptativos, componentes ligadas e um motor de OCR público podem ser compreendidos, verificados e corridos de novo por qualquer pessoa com um portátil, e cada parâmetro que importa é uma fracção da página e não um número mágico. Um modelo treinado teria provavelmente melhores resultados; não poderia ser inspeccionado, e não poderia ser reproduzido sem o seu conjunto de treino. Para um corpus pequeno e mal digitalizado, a legibilidade do método vale mais do que os últimos pontos de exactidão.</p>
        <h3 style="margin-top:26px">Limitações, ditas com clareza</h3>
        <p style="margin-top:8px">Não existe verdade de referência anotada à mão para este corpus, pelo que não se apresenta nenhum valor formal de precisão. Verificações por amostragem sugerem que cerca de uma região candidata em cada cinco é um falso alarme, na maior parte das vezes um título de várias linhas a negrito lido como desenho, ou um bloco denso e esborratado de texto lido como fotografia. As primeiras etiquetas da etapa 3 são a camada mais fraca; em páginas muito esborratadas, letras desenhadas e fotografias confundem-se com regularidade. As caixas são generosas em vez de justas, porque o passo de fusão prefere manter uma legenda com o seu desenho a separá-los. A confiança do OCR é alta nas páginas limpas e baixa nas esborratadas, e nem sempre se distinguem de antemão.</p>
        <h3 style="margin-top:26px">Reproduzir</h3>
        <p style="margin-top:8px">Os três scripts acima são o detector completo. Com um clone do repositório:</p>
<pre>pip install pypdfium2 opencv-python-headless numpy pytesseract
# O próprio Tesseract e o modelo de português: apt install tesseract-ocr tesseract-ocr-por

python3 rasterise.py /caminho/do/repositorio pages/   # etapa 2: 487 bitmaps + pages.json
python3 segment.py   pages/ regions.json              # etapa 3: regiões candidatas
python3 ocr.py       pages/ regions.json text/        # etapa 4: um .txt por página</pre>
        <div class="actions"><button class="btn" data-save="all">Guardar os três scripts</button></div>
      </div>
""",

"about": """
    <div class="head"><h2>Sobre</h2></div>
    <div class="cols">
      <div>
        <dl>
          <dt>O projecto</dt>
          <dd>COMBAT — Computational OCR/ATR Methods for <em>Combate</em>: Comics, Images and Text — aplica a leitura por máquina a um jornal que lhe resiste, e trata o seu conteúdo gráfico como evidência e não como decoração. As digitalizações, o código, o catálogo e este site vivem num único repositório público.</dd>
          <dt>Quem o fez</dt>
          <dd>Desenvolvido e mantido por Pedro João Oliveira.</dd>
          <dt>Licença</dt>
          <dd>O código e o catálogo são publicados sob a GNU General Public License v3.0. As digitalizações do jornal continuam sujeitas aos direitos dos seus detentores e são reproduzidas para investigação e estudo.</dd>
        </dl>
      </div>
      <div>
        <dl>
          <dt>O jornal</dt>
          <dd>O <em>Combate</em> publicou-se de Junho de 1974, semanas depois da Revolução dos Cravos, até 1978. Descrevia-se como um jornal dos próprios trabalhadores, e tinha esse aspecto: títulos desenhados à mão, desenhos de colaboradores, panfletos e comunicados reimpressos, e uma paginação que mudava de página para página. A sua linha, impressa sob o cabeçalho do primeiro número, era que a emancipação dos trabalhadores é obra dos próprios trabalhadores.</dd>
          <dt>Fontes</dt>
          <dd>Colecção em papel: Biblioteca Nacional de Portugal. Cópias digitais: Marxists Internet Archive. Como as digitalizações são de má qualidade, tudo o que seja usado como evidência deve ser confrontado com o exemplar em papel.</dd>
          <dt>Como citar</dt>
          <dd><pre class="paper" style="margin-top:4px">Oliveira, P. J. COMBAT: Computational OCR/ATR
Methods for Combate — Comics, Images and Text.
Repositório GitHub, 2026.</pre></dd>
        </dl>
      </div>
    </div>
    <div class="actions">
      <a class="btn solid" href="__REPO__">Repositório no GitHub</a>
    </div>
""",

"footer": """COMBAT, um projecto sobre o jornal <em>Combate</em> (1974–1978). As páginas são transmitidas a partir do <a href="__REPO__">repositório do projecto</a>. Código e catálogo sob GPL-3.0.""",
}

BLOCKS = {k: v.replace("__REPO__", REPO) for k, v in BLOCKS.items()}
