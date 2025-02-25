# Installation et Lancement de VILA

Ce guide explique comment installer et lancer **VILA** sur la carte **Jetson Orin Nano**.

Nous avons suivi le tutoriel du laboratoire NVIDIA pour réaliser cette installation : [https://www.jetson-ai-lab.com/tutorial_nano-vlm.html](#)

## 1. Installation de NanoLLM et VILA

Exécutez la commande suivante pour installer et exécuter **NanoLLM** et **VILA** :

```bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 64 \
    --max-new-tokens 32
```
Après installation, le modèle VILA sera automatiquement lancé et vous pourrez le questionner.

## 2. Questionner VILA sur une image

**Remarque :** Les images doivent être placées dans le répertoire `jetson-containers/data/images/`.

Pour lui poser des questions, écrire dans l'interface ouverte après lancement :
```bash
>> PROMPT: /data/images/mon_image.png

>> PROMPT: Je pose ma question ici.
```

N'hésitez pas à réinitialiser le questionnement pour fournir une autre image ou éviter que le modèle ne se base sur ses réponses précédentes à l'aide de **reset** :
```bash
>> PROMPT: reset
```

### Préparer des prompts en avance

Vous pouvez structurer vos questions en amont comme suit :

```bash
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
```

📌 **Note :**
- Le premier prompt doit contenir le chemin de l'image à analyser.
- Le mot-clé `reset` permet de réinitialiser l'historique de discussion et de soumettre une nouvelle image.

## 3. Questionner VILA en mode direct

```bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.agents.video_query --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 256 \
    --max-new-tokens 32 \
    --video-input /dev/video0 \
    --video-output webrtc://@:8554/output
```

---

Ce guide fournit une procédure claire pour utiliser **VILA** sur la **Jetson Orin Nano**. Pour plus de détails, reportez-vous à la documentation officielle de NVIDIA.
