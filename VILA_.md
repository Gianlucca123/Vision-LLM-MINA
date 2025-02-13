## Installation et lancement de VILA
Ce README concerne l'installation et le lancement de VILA sur la carte Jetson Orin Nano

Nous avons utilisé le tutoriel du lab nvidia pour réaliser cette installation : TODO LIEN

1. Installation de NanoLLM et VILA
???
'''bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
'''

2. Questionner VILA sur une image

Il est important de noter que les images doivent se trouver dans le répertoir jetson-containers/data/images/.

'''bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 64 \
    --max-new-tokens 32
'''


Il est possible de préparer les prompts en avance comme suit :
'''bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 256 \
    --max-new-tokens 32 \
    --prompt '/data/images/hoover.jpg' \
    --prompt 'what does the road sign say?' \
    --prompt 'what kind of environment is it?' \
    --prompt 'reset' \
    --prompt '/data/images/lake.jpg' \
    --prompt 'please describe the scene.' \
    --prompt 'are there any hazards to be aware of?'
'''

A savoir que le premier prompt doit etre le chemin de l'image à fournir et que reset permet d'effacer l'historique de discution et de fournir une nouvelle image.

3. Questionner VILA en mode direct

'''bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.agents.video_query --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 256 \
    --max-new-tokens 32 \
    --video-input /dev/video0 \
    --video-output webrtc://@:8554/output
'''

