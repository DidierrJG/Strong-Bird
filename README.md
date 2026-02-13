<h1>
  Strong Bird
</h1>

<p>
  Strong Bird es un juego inspirado en la mecánica de Flappy Bird, desarrollado en Python como proyecto de aprendizaje.
  El juego integra visión por computadora para permitir que el jugador controle el personaje usando movimientos corporales detectados con la cámara web.
</p>

<h2>
  ¿Como funciona el juego?
</h2>

<p>
  El jugador controla el salto del pájaro mediante movimientos laterales del cuerpo:
  <ul>
    <li>Cuando el sistema detecta una elevación lateral, el pájaro salta.</li>
    <li>Si el jugador pierde, debe realizar otra elevación lateral para reiniciar la partida.</li>
  </ul>
  El movimiento es detectado en tiempo real usando la cámara del usuario.
</p>

<h2>
  Tecnologias utilizadas
</h2>

<ul>
  <li>Python</li>
  <li>Pygame</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
</ul>

<h2>
  Instalacion
</h2>

<p>
  <strong>1. Clonar repositorio</strong>
</p>

```
git clone https://github.com/DidierrJG/Strong-Bird
```

<p>
  <strong>2. Instalar dependecias</strong>
</p>

```
pip install pygame opencv-python mediapipe==0.10.14
```

<p>
  <strong>3. Ejecutar el juego</strong>
</p>

```
python main.py
```

<h2>
  Requisitos
</h2>

<ul>
  <li>Python 3.11</li>
  <li>Cámara web funcional</li>
  <li>Buena iluminación (para mejor detección del movimiento)</li>
</ul>

<h2>
  Assets
</h2>

<ul>
  <li>Parte de los sprites fueron creados manualmente para este proyecto.</li>
  <li>El fondo proviene del juego original Flappy Bird y se usa únicamente con fines educativos.</li>
</ul>
