import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { 'raw_document': { 'text': text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    if not text_to_analyse.strip():
        return { 'anger': None, 'disgust': None, 'fear': None,'joy': None, 'sadness': None, 'dominant_emotion': None
        }  
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)  
    if response.status_code == 200:
        predictions = formatted_response['emotionPredictions'][0]['emotion']  
        anger_score = predictions['anger']
        disgust_score = predictions['disgust']
        fear_score = predictions['fear']
        joy_score = predictions['joy']
        sadness_score = predictions['sadness'] 
        emotion_scores = { 'anger': anger_score, 'disgust': disgust_score,'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None 
        dominant_emotion = None
    return {'anger': anger_score,'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 
            'dominant_emotion': dominant_emotion
    }
