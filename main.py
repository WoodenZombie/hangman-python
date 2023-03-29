"""
Game "Hangman" as a console application
Written by Tania Velegura
Work started: 20.04.2021
"""

import random
import time 


hangman = [
"",
"""
         \n
          \n
          \n
          \n
          \n
          \n
          \n
 ____\n
""",
"""
   ______\n
   |      \n
   |      \n
   |      \n
   |      \n
   |      \n
   |      \n
 __|__\n
""",
"""
   ______\n
   |    |  \n
   |    |  \n
   |      \n
   |      \n
   |      \n
   |      \n
 __|__\n
""",
"""
   ______ \n
   |    |  \n
   |    |  \n
   |    O   \n
   |      \n
   |      \n
   |      \n
 __|__\n
""",
"""
   ______ \n
   |    |  \n
   |    |  \n
   |    O   \n
   |   /|\  \n
   |      \n
   |      \n
 __|__\n
""",
"""
   ______  \n
   |    |  \n
   |    |  \n
   |    O  \n
   |   /|\ \n
   |   / \ \n
   |      \n
 __|__\n
""",
]

# 1000 of the most popular words in each language

words = ['people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family', 'government', 'health', 'system', 'computer', 'meat', 'year', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding', 'theory', 'law', 'bird', 'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 'economics', 'love', 'internet', 'television', 'science', 'library', 'nature', 'fact', 'product', 'idea', 'temperature', 'investment', 'area', 'society', 'activity', 'story', 'industry', 'media', 'thing', 'oven', 'community', 'definition', 'safety', 'quality', 'development', 'language', 'management', 'player', 'variety', 'video', 'week', 'security', 'country', 'exam', 'movie', 'organization', 'equipment', 'physics', 'analysis', 'policy', 'series', 'thought', 'basis', 'boyfriend', 'direction', 'strategy', 'technology', 'army', 'camera', 'freedom', 'paper', 'environment', 'child', 'instance', 'month', 'truth', 'marketing', 'university', 'writing', 'article', 'department', 'difference', 'goal', 'news', 'audience', 'fishing', 'growth', 'income', 'marriage', 'user', 'combination', 'failure', 'meaning', 'medicine', 'philosophy', 'teacher', 'communication', 'night', 'chemistry', 'disease', 'disk', 'energy', 'nation', 'road', 'role', 'soup', 'advertising', 'location', 'success', 'addition', 'apartment', 'education', 'math', 'moment', 'painting', 'politics', 'attention', 'decision', 'event', 'property', 'shopping', 'student', 'wood', 'competition', 'distribution', 'entertainment', 'office', 'population', 'president', 'unit', 'category', 'cigarette', 'context', 'introduction', 'opportunity', 'performance', 'driver', 'flight', 'length', 'magazine', 'newspaper', 'relationship', 'teaching', 'cell', 'dealer', 'finding', 'lake', 'member', 'message', 'phone', 'scene', 'appearance', 'association', 'concept', 'customer', 'death', 'discussion', 'housing', 'inflation', 'insurance', 'mood', 'woman', 'advice', 'blood', 'effort', 'expression', 'importance', 'opinion', 'payment', 'reality', 'responsibility', 'situation', 'skill', 'statement', 'wealth', 'application', 'city', 'county', 'depth', 'estate', 'foundation', 'grandmother', 'heart', 'perspective', 'photo', 'recipe', 'studio', 'topic', 'collection', 'depression', 'imagination', 'passion', 'percentage', 'resource', 'setting', 'agency', 'college', 'connection', 'criticism', 'debt', 'description', 'memory', 'patience', 'secretary', 'solution', 'administration', 'aspect', 'attitude', 'director', 'personality', 'psychology', 'recommendation', 'response', 'selection', 'storage', 'version', 'alcohol', 'argument', 'complaint', 'contract', 'emphasis', 'highway', 'loss', 'membership', 'possession', 'preparation', 'steak', 'union', 'agreement', 'cancer', 'currency', 'employment', 'engineering', 'entry', 'interaction', 'mixture', 'preference', 'region', 'republic', 'tradition', 'virus', 'actor', 'classroom', 'delivery', 'device', 'difficulty', 'drama', 'election', 'engine', 'football', 'guidance', 'hotel', 'owner', 'priority', 'protection', 'suggestion', 'tension', 'variation', 'anxiety', 'atmosphere', 'awareness', 'bath', 'bread', 'candidate', 'climate', 'comparison', 'confusion', 'construction', 'elevator', 'emotion', 'employee', 'employer', 'guest', 'height', 'leadership', 'mall', 'manager', 'operation', 'recording', 'sample', 'transportation', 'charity', 'cousin', 'disaster', 'editor', 'efficiency', 'excitement', 'extent', 'feedback', 'guitar', 'homework', 'leader', 'mom', 'outcome', 'permission', 'presentation', 'promotion', 'reflection', 'refrigerator', 'resolution', 'revenue', 'session', 'singer', 'tennis', 'basket', 'bonus', 'cabinet', 'childhood', 'church', 'clothes', 'coffee', 'dinner', 'drawing', 'hair', 'hearing', 'initiative', 'judgment', 'lab', 'measurement', 'mode', 'mud', 'orange', 'poetry', 'police', 'possibility', 'procedure', 'queen', 'ratio', 'relation', 'restaurant', 'satisfaction', 'sector', 'signature', 'significance', 'song', 'tooth', 'town', 'vehicle', 'volume', 'wife', 'accident', 'airport', 'appointment', 'arrival', 'assumption', 'baseball', 'chapter', 'committee', 'conversation', 'database', 'enthusiasm', 'error', 'explanation', 'farmer', 'gate', 'girl', 'hall', 'historian', 'hospital', 'injury', 'instruction', 'maintenance', 'manufacturer', 'meal', 'perception', 'pie', 'poem', 'presence', 'proposal', 'reception', 'replacement', 'revolution', 'river', 'son', 'speech', 'tea', 'village', 'warning', 'winner', 'worker', 'writer', 'assistance', 'breath', 'buyer', 'chest', 'chocolate', 'conclusion', 'contribution', 'cookie', 'courage', 'dad', 'desk', 'drawer', 'establishment', 'examination', 'garbage', 'grocery', 'honey', 'impression', 'improvement', 'independence', 'insect', 'inspection', 'inspector', 'king', 'ladder', 'menu', 'penalty', 'piano', 'potato', 'profession', 'professor', 'quantity', 'reaction', 'requirement', 'salad', 'sister', 'supermarket', 'tongue', 'weakness', 'wedding', 'affair', 'ambition', 'analyst', 'apple', 'assignment', 'assistant', 'bathroom', 'bedroom', 'beer', 'birthday', 'celebration', 'championship', 'cheek', 'client', 'consequence', 'departure', 'diamond', 'dirt', 'ear', 'fortune', 'friendship', 'funeral', 'gene', 'girlfriend', 'hat', 'indication', 'intention', 'lady', 'midnight', 'negotiation', 'obligation', 'passenger', 'pizza', 'platform', 'poet', 'pollution', 'recognition', 'reputation', 'shirt', 'sir', 'speaker', 'stranger', 'surgery', 'sympathy', 'tale', 'throat', 'trainer', 'uncle', 'youth', 'time', 'work', 'film', 'water', 'money', 'example', 'while', 'business', 'study', 'game', 'life', 'form', 'air', 'day', 'place', 'number', 'part', 'field', 'fish', 'back', 'process', 'heat', 'hand', 'experience', 'job', 'book', 'end', 'point', 'type', 'home', 'economy', 'value', 'body', 'market', 'guide', 'interest', 'state', 'radio', 'course', 'company', 'price', 'size', 'card', 'list', 'mind', 'trade', 'line', 'care', 'group', 'risk', 'word', 'fat', 'force', 'key', 'light', 'training', 'name', 'school', 'top', 'amount', 'level', 'order', 'practice', 'research', 'sense', 'service', 'piece', 'web', 'boss', 'sport', 'fun', 'house', 'page', 'term', 'test', 'answer', 'sound', 'focus', 'matter', 'kind', 'soil', 'board', 'oil', 'picture', 'access', 'garden', 'range', 'rate', 'reason', 'future', 'site', 'demand', 'exercise', 'image', 'case', 'cause', 'coast', 'action', 'age', 'boat', 'record', 'result', 'section', 'building', 'mouse', 'cash', 'class', 'nothing', 'period', 'plan', 'store', 'tax', 'side', 'subject', 'space', 'rule', 'stock', 'weather', 'chance', 'figure', 'man', 'model', 'source', 'beginning', 'earth', 'program', 'chicken', 'design', 'feature', 'head', 'material', 'purpose', 'question', 'rock', 'salt', 'act', 'birth', 'car', 'dog', 'object', 'scale', 'sun', 'note', 'profit', 'rent', 'speed', 'style', 'war', 'bank', 'craft', 'half', 'inside', 'outside', 'standard', 'bus', 'exchange', 'eye', 'fire', 'position', 'pressure', 'stress', 'advantage', 'benefit', 'box', 'frame', 'issue', 'step', 'cycle', 'face', 'item', 'metal', 'paint', 'review', 'room', 'screen', 'structure', 'view', 'account', 'ball', 'discipline', 'medium', 'share', 'balance', 'bit', 'bottom', 'choice', 'gift', 'impact', 'machine', 'shape', 'tool', 'wind', 'address', 'average', 'career', 'culture', 'morning', 'pot', 'sign', 'table', 'task', 'condition', 'contact', 'credit', 'egg', 'hope', 'ice', 'network', 'north', 'square', 'attempt', 'date', 'effect', 'link', 'post', 'star', 'voice', 'capital', 'challenge', 'friend', 'self', 'shot', 'brush', 'couple', 'debate', 'exit', 'front', 'function', 'lack', 'living', 'plant', 'plastic', 'spot', 'summer', 'taste', 'theme', 'track', 'wing', 'brain', 'button', 'click', 'desire', 'foot', 'gas', 'influence', 'notice', 'rain', 'wall', 'base', 'damage', 'distance', 'feeling', 'pair', 'savings', 'staff', 'sugar', 'target', 'text', 'animal', 'author', 'budget', 'discount', 'file', 'ground', 'lesson', 'minute', 'officer', 'phase', 'reference', 'register', 'sky', 'stage', 'stick', 'title', 'trouble', 'bowl', 'bridge', 'campaign', 'character', 'club', 'edge', 'evidence', 'fan', 'letter', 'lock', 'maximum', 'novel', 'option', 'pack', 'park', 'plenty', 'quarter', 'skin', 'sort', 'weight', 'baby', 'background', 'carry', 'dish', 'factor', 'fruit', 'glass', 'joint', 'master', 'muscle', 'red', 'strength', 'traffic', 'trip', 'vegetable', 'appeal', 'chart', 'gear', 'ideal', 'kitchen', 'land', 'log', 'mother', 'net', 'party', 'principle', 'relative', 'sale', 'season', 'signal', 'spirit', 'street', 'tree', 'wave', 'belt', 'bench', 'commission', 'copy', 'drop', 'minimum', 'path', 'progress', 'project', 'sea', 'south', 'status', 'stuff', 'ticket', 'tour', 'angle', 'blue', 'breakfast', 'confidence', 'daughter', 'degree', 'doctor', 'dot', 'dream', 'duty', 'essay', 'father', 'fee', 'finance', 'hour', 'juice', 'limit', 'luck', 'milk', 'mouth', 'peace', 'pipe', 'seat', 'stable', 'storm', 'substance', 'team', 'trick', 'afternoon', 'bat', 'beach', 'blank', 'catch', 'chain', 'consideration', 'cream', 'crew', 'detail', 'gold', 'interview', 'kid', 'mark', 'match', 'mission', 'pain', 'pleasure', 'score', 'screw', 'sex', 'shop', 'shower', 'suit', 'tone', 'window', 'agent', 'band', 'block', 'bone', 'calendar', 'cap', 'coat', 'contest', 'corner', 'court', 'cup', 'district', 'door', 'east', 'finger', 'garage', 'guarantee', 'hole', 'hook', 'implement', 'layer', 'lecture', 'lie', 'manner', 'meeting', 'nose', 'parking', 'partner', 'profile', 'respect', 'rice', 'routine', 'schedule', 'swimming', 'telephone', 'tip', 'winter', 'airline', 'bag', 'battle', 'bed', 'bill', 'bother', 'cake', 'code', 'curve', 'designer', 'dimension', 'dress', 'ease', 'emergency', 'evening', 'extension', 'farm', 'fight', 'gap', 'grade', 'holiday', 'horror', 'horse', 'host', 'husband', 'loan', 'mistake', 'mountain', 'nail', 'noise', 'occasion', 'package', 'patient', 'pause', 'phrase', 'proof', 'race', 'relief', 'sand', 'sentence', 'shoulder', 'smoke', 'stomach', 'string', 'tourist', 'towel', 'vacation', 'west', 'wheel', 'wine', 'arm', 'aside', 'associate', 'bet', 'blow', 'border', 'branch', 'breast', 'brother', 'buddy', 'bunch', 'chip', 'coach', 'cross', 'document', 'draft', 'dust', 'expert', 'floor', 'god', 'golf', 'habit', 'iron', 'judge', 'knife', 'landscape', 'league', 'mail', 'mess', 'native', 'opening', 'parent', 'pattern', 'pin', 'pool', 'pound', 'request', 'salary', 'shame', 'shelter', 'shoe', 'silver', 'tackle', 'tank', 'trust', 'assist', 'bake', 'bar', 'bell', 'bike', 'blame', 'boy', 'brick', 'chair', 'closet', 'clue', 'collar', 'comment', 'conference', 'devil', 'diet', 'fear', 'fuel', 'glove', 'jacket', 'lunch', 'monitor', 'mortgage', 'nurse', 'pace', 'panic', 'peak', 'plane', 'reward', 'row', 'sandwich', 'shock', 'spite', 'spray', 'surprise', 'till', 'transition', 'weekend', 'welcome', 'yard', 'alarm', 'bend', 'bicycle', 'bite', 'blind', 'bottle', 'cable', 'candle', 'clerk', 'cloud', 'concert', 'counter', 'flower', 'grandfather', 'harm', 'knee', 'lawyer', 'leather', 'load', 'mirror', 'neck', 'pension', 'plate', 'purple', 'ruin', 'ship', 'skirt', 'slice', 'snow', 'specialist', 'stroke', 'switch', 'trash', 'tune', 'zone', 'anger', 'award', 'bid', 'bitter', 'boot', 'bug', 'camp', 'candy', 'carpet', 'cat', 'champion', 'channel', 'clock', 'comfort', 'cow', 'crack', 'engineer', 'entrance', 'fault', 'grass', 'guy', 'hell', 'highlight', 'incident', 'island', 'joke', 'jury', 'leg', 'lip', 'mate', 'motor', 'nerve', 'passage', 'pen', 'pride', 'priest', 'prize', 'promise', 'resident', 'resort', 'ring', 'roof', 'rope', 'sail', 'scheme', 'script', 'sock', 'station', 'toe', 'tower', 'truck', 'witness', 'use', 'look', 'help', 'public', 'start', 'human', 'major', 'cut', 'show', 'second', 'individual', 'turn', 'guard', 'offer', 'alternative', 'dance', 'excuse', 'cold', 'commercial', 'purchase', 'deal', 'worth', 'fall', 'reserve', 'rest', 'watch', 'break', 'visit', 'cover', 'report', 'rise', 'walk', 'junior', 'lift', 'gain', 'lead', 'press', 'ride', 'secret', 'spring', 'display', 'flow', 'chemical', 'dump', 'conflict', 'jump', 'kick', 'opposite', 'abuse', 'burn', 'deposit', 'print', 'raise', 'sleep', 'advance', 'kill', 'tap', 'win', 'attack', 'claim', 'drink', 'guess', 'raw', 'dead', 'slide', 'strip', 'wish', 'command', 'equivalent', 'hunt', 'march', 'smell', 'survey', 'tie', 'adult', 'escape', 'hate', 'scratch', 'strike', 'laugh', 'mobile', 'respond', 'strain', 'struggle', 'train', 'crash', 'fold', 'permit', 'quote', 'roll', 'sink', 'slip', 'spare', 'suspect', 'sweet', 'swing', 'twist', 'male', 'mine', 'prompt', 'regret', 'bear', 'brilliant', 'delay', 'female', 'hurry', 'kiss', 'neat', 'punch', 'quit', 'reply', 'smile', 'spell', 'stretch', 'stupid', 'tear', 'wrap', 'yesterday']
words_rus = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'вопрос', 'лицо', 'глаз', 'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова', 'система', 'вид', 'конец', 'отношение', 'город', 'часть', 'женщина', 'проблема', 'земля', 'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец', 'история', 'нога', 'вода', 'война', 'возможность', 'компания', 'результат', 'дверь', 'бог', 'народ', 'область', 'число', 'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд', 'деньга', 'уровень', 'начало', 'государство', 'стол', 'средство', 'связь', 'имя', 'президент', 'форма', 'путь', 'организация', 'качество', 'действие', 'статья', 'общество', 'ситуация', 'деятельность', 'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель', 'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок', 'предприятие', 'партия', 'роль', 'смысл', 'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр', 'внимание', 'производство', 'квартира', 'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната', 'семья', 'сын', 'смерть', 'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор', 'окно', 'ответ', 'совет', 'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план', 'проект', 'глава', 'материал', 'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль', 'наука', 'документ', 'неделя', 'вещь', 'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'член', 'ход', 'стена', 'директор', 'плечо', 'опыт', 'встреча', 'принцип', 'событие', 'структура', 'количество', 'товарищ', 'создание', 'значение', 'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример', 'лес', 'исследование', 'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат', 'представитель', 'борьба', 'использование', 'шаг', 'игра', 'участие', 'территория', 'край', 'размер', 'номер', 'район', 'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь', 'направление', 'позиция', 'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик', 'фильм', 'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт', 'церковь', 'завод', 'фирма', 'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух', 'музыка', 'способ', 'хозяин', 'поле', 'доллар', 'память', 'природа', 'дерево', 'оценка', 'объем', 'картина', 'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант', 'берег', 'модель', 'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол', 'зрение', 'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство', 'солнце', 'автомобиль', 'родитель', 'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'ум', 'море', 'удар', 'знание', 'солдат', 'миллион', 'строительство', 'технология', 'председатель', 'сон', 'сознание', 'бумага', 'реформа', 'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок', 'услуга', 'поэт', 'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет', 'представление', 'площадь', 'генерал', 'господин', 'дочь', 'понятие', 'кабинет', 'безопасность', 'фонд', 'сфера', 'папа', 'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика', 'сумма', 'контроль', 'парень', 'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь', 'нос', 'волос', 'ухо', 'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето', 'камень', 'здание', 'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня', 'депутат', 'проведение', 'рот', 'масса', 'комиссия', 'цвет', 'рассказ', 'функция', 'определение', 'мужик', 'обеспечение', 'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение', 'победа', 'товар', 'воля', 'зона', 'предел', 'целое', 'личность', 'офицер', 'влияние', 'поддержка', 'ответственность', 'цветок', 'праздник', 'немец', 'бой', 'сестра', 'господь', 'учитель', 'многое', 'рамка', 'практика', 'показатель', 'метр', 'войско', 'частность', 'особенность', 'снег', 'комитет', 'налог', 'акт', 'отдел', 'карман', 'вывод', 'норма', 'читатель', 'этап', 'сравнение', 'прошлое', 'фамилия', 'кухня', 'заявление', 'доля', 'пункт', 'студент', 'учет', 'впечатление', 'доход', 'вирус', 'клетка', 'удовольствие', 'теория', 'враг', 'собрание', 'бутылка', 'расчет', 'го', 'режим', 'множество', 'клуб', 'попытка', 'зуб', 'сеть', 'семь', 'министерство', 'прием', 'боль', 'сожаление', 'кожа', 'субъект', 'знак', 'актер', 'ресурс', 'акция', 'газ', 'журналист', 'звук', 'передача', 'здоровье', 'администрация', 'болезнь', 'детство', 'мастер', 'выборы', 'зима', 'подход', 'поиск', 'механизм', 'выражение', 'скорость', 'ощущение', 'стоимость', 'коридор', 'ошибка', 'лидер', 'карта', 'заседание', 'глубина', 'хлеб', 'поверхность', 'энергия', 'нарушение', 'реализация', 'революция', 'поведение', 'профессор', 'исполнение', 'заместитель', 'суть', 'станция', 'реакция', 'десяток', 'столица', 'формирование', 'поколение', 'дума', 'существование', 'продажа', 'список', 'способность', 'противник', 'схема', 'долг', 'режиссер', 'отличие', 'колено', 'дед', 'свойство', 'этаж', 'секунда', 'фактор', 'житель', 'явление', 'высота', 'сосед', 'усилие', 'рождение', 'расход', 'остров', 'фигура', 'наличие', 'дядя', 'милиция', 'растение', 'существо', 'черт', 'бабушка', 'законодательство', 'собственность', 'отрасль', 'слеза', 'волна', 'стекло', 'традиция', 'январь', 'оборудование', 'зависимость', 'фраза', 'декабрь', 'сведение', 'трубка', 'сентябрь', 'университет', 'командир', 'храм', 'повышение', 'стиль', 'артист', 'больница', 'одежда', 'охрана', 'водка', 'кодекс', 'имущество', 'птица', 'переход', 'красота', 'клиент', 'толпа', 'адрес', 'отделение', 'октябрь', 'чудо', 'счастие', 'улыбка', 'ужас', 'аппарат', 'корабль', 'родина', 'животное', 'черта', 'известие', 'понимание', 'тень', 'апрель', 'коллега', 'преступление', 'рыба', 'кресло', 'запах', 'выставка', 'князь', 'фотография', 'весна', 'помещение', 'эпоха', 'занятие', 'произведение', 'концерт', 'ладонь', 'дама', 'сомнение', 'американец', 'середина', 'зарплата', 'тайна', 'запад', 'июнь', 'беседа', 'фронт', 'поезд', 'должность', 'баба', 'промышленность', 'музей', 'судья', 'получение', 'полковник', 'зритель', 'секретарь', 'установка', 'поток', 'ценность', 'образец', 'страница', 'перспектива', 'трава', 'чиновник', 'мозг', 'сотня', 'лагерь', 'выступление', 'оборона', 'постановление', 'честь', 'настроение', 'кровать', 'характеристика', 'обязанность', 'шея', 'крыша', 'появление', 'учреждение', 'признак', 'труба', 'жертва', 'беда', 'фон', 'организм', 'ученик', 'заключение', 'выполнение', 'канал', 'исключение', 'дача', 'соглашение', 'осень', 'польза', 'стул', 'июль', 'дождь', 'сутки', 'еврей', 'конкурс', 'открытие', 'телевизор', 'лошадь', 'температура', 'приказ', 'лестница', 'реклама', 'спор', 'подруга', 'угроза', 'конфликт', 'изучение', 'вино', 'концепция', 'достижение', 'сообщение', 'объединение', 'обстановка', 'костюм', 'ключ', 'ресторан', 'назначение', 'царь', 'воспоминание', 'увеличение', 'вкус', 'мероприятие', 'лоб', 'слой', 'восток', 'последствие', 'принятие', 'сотрудничество', 'нефть', 'слух', 'бок', 'переговоры', 'тюрьма', 'кандидат', 'просьба', 'реальность', 'подарок', 'категория', 'потребность', 'быль', 'редакция', 'очко', 'километр', 'губернатор', 'новость', 'инструмент', 'потеря', 'взаимодействие', 'звонок', 'кусок', 'капитал', 'грех', 'перевод', 'партнер', 'ноябрь', 'молодежь', 'тишина', 'творчество', 'книжка', 'мясо', 'масло', 'деталь', 'инженер', 'оплата', 'эксперт', 'кремль', 'февраль', 'следствие', 'пьеса', 'билет', 'урок', 'коллектив', 'устройство', 'палата', 'площадка', 'опасность', 'пропасть', 'воздействие', 'разница', 'родственник', 'сезон', 'издание', 'человечество', 'снижение', 'запас', 'крик', 'публика', 'вещество', 'экран', 'эффект', 'ящик', 'ракета', 'водитель', 'пакет', 'зеркало', 'вес', 'дно', 'вагон', 'убийство', 'тон', 'щека', 'дурак', 'длина', 'давление', 'двигатель', 'камера', 'обращение', 'формула', 'запись', 'крыло', 'поездка', 'гостиница', 'колесо', 'разрешение', 'торговля', 'академия', 'доклад', 'общение', 'присутствие', 'процедура', 'испытание', 'нож', 'проверка', 'коммунист', 'цифра', 'полет', 'стакан', 'эффективность', 'обучение', 'портрет', 'достоинство', 'рассмотрение', 'владелец', 'жилье', 'компьютер', 'корень', 'смена', 'доказательство', 'кадр', 'лейтенант', 'признание', 'темнота', 'пистолет', 'наблюдение', 'мост', 'ремонт', 'истина', 'вход', 'политик', 'живот', 'кредит', 'шум', 'обед', 'недостаток', 'памятник', 'вершина', 'серия', 'эксперимент', 'сущность', 'транспорт', 'инициатива', 'активность', 'конференция', 'кулак', 'доска', 'ожидание', 'платье', 'смех', 'отказ', 'сбор', 'пенсия', 'буква', 'порог', 'автобус', 'воспитание', 'производитель', 'полоса', 'риск', 'пиво', 'корпус', 'штаб', 'кольцо', 'постель', 'выпуск', 'дворец', 'брак', 'прокурор', 'печать', 'окончание', 'автомат', 'тенденция', 'следователь', 'штат', 'куст', 'старуха', 'описание', 'психология', 'шутка', 'съезд', 'ставка', 'забота', 'величина', 'версия', 'мешок', 'конструкция', 'контакт', 'шанс', 'лодка', 'редактор', 'заказ', 'кофе', 'рубеж', 'статус', 'спорт', 'покой', 'кризис', 'взрыв', 'профессия', 'дым', 'металл', 'сапог', 'диван', 'интернет', 'почва', 'лед', 'подразделение', 'минимум', 'конь', 'дружба', 'вина', 'замок', 'мечта', 'сигнал', 'талант', 'мгновение', 'столик', 'затрата', 'золото', 'миг', 'плата', 'подъезд', 'масштаб', 'обсуждение', 'сделка', 'обязательство', 'расстояние', 'отдых', 'телевидение', 'тетя', 'яблоко', 'свидетель', 'монастырь', 'чтение', 'параметр', 'кампания', 'помощник', 'полк', 'мощность', 'сюжет', 'потолок', 'регистрация', 'майор', 'эксплуатация', 'озеро', 'новое', 'атмосфера', 'премия', 'совесть', 'предприниматель', 'мальчишка', 'дочка', 'приятель', 'начальство', 'препарат', 'село', 'обработка', 'танк', 'милиционер', 'ручка', 'возвращение', 'прокуратура', 'ворота', 'молоко', 'еда', 'сказка', 'краска', 'хвост', 'сигарета', 'введение', 'покупатель', 'поворот', 'москвич', 'ограничение', 'инвестиция', 'нация', 'набор', 'поселок', 'дыхание', 'адвокат', 'сумка', 'пресса', 'корреспондент', 'песок', 'удивление', 'потребитель', 'указание', 'изображение', 'счастье', 'мэр', 'согласие', 'действительность', 'планета', 'агентство', 'танец', 'библиотека', 'финансирование', 'объяснение', 'распределение', 'конституция', 'таблица', 'поэзия', 'термин', 'прибыль', 'стандарт', 'восторг', 'гибель', 'изделие', 'темп', 'вооружение', 'осуществление', 'уход', 'чемпионат', 'молитва', 'контракт', 'философия', 'горло', 'оборот', 'кость', 'ведомство', 'преимущество', 'мина', 'полномочие']


def game_eng():
    word = words[random.randrange(0, len(words))]
    game_word = list(len(word)*"_")
    guessed_letters = []
    guess_number = 0

    time.sleep(1)
    print("So we are ready to start! Your word is\n")
    for i in game_word:
        print(i, end=" ")
    print("\n")

    while True:
        letter = input("Please, enter the letter: ")
        time.sleep(1)
        while len(letter) != 1:
            letter = input("Invalid input. Please try again. You need to type in a LETTER ")
        while letter in guessed_letters or letter in game_word:
            letter = input("You have already guessed this letter. Please try the new one. ")
        if letter in word:
            game_word[word.index(letter)] = letter
            print("\nYou nailed it! This letter IS in the game word")        
        else:
            print("\nSorry, but you guessed wrong.")
            guess_number += 1
            guessed_letters.append(letter)
        time.sleep(1)
        print(hangman[guess_number])
        for i in range(len(word)):
            if word[i] == letter:
                game_word[i] = letter
        print(" ".join(game_word))
        print("Guessed letters: " + ", ".join(guessed_letters) + "\n")
        if "_" not in game_word:
            print("You won! The word was "+ word.upper())
            break
        elif guess_number == 6:
            print("Unfortunately, you lost. The word was " + word)
            break
    
    print("Do you want to try again? Yes/no")
    answer = input("")
    while answer not in ["Yes", "no"]:
        print("I can't quite understand you. Please type in answer in format Yes or no")
        print("Do you want to try again? Yes/no")
        answer = input("")
    if answer == "Yes".lower():
        game_eng()

def game_rus():
    word = words_rus[random.randrange(0, len(words_rus))]
    game_word = list(len(word)*"_")
    guessed_letters = []
    guess_number = 0

    time.sleep(1)
    print("И так, время начинать! Слово для этой игры:\n")
    for i in game_word:
        print(i, end=" ")
    print("\n")

    while True:
        letter = input("Пожалуйста, введите букву: ")
        time.sleep(1)
        while len(letter) != 1:
            letter = input("Неправильный ввод. Пожалуйста, попробуйте ещё раз. Вам нужно ввести БУКВУ")
        while letter in guessed_letters or letter in game_word:
            letter = input("Вы уже угадывали эту букву. Попробуйте ещё раз.")
        if letter in word:
            game_word[word.index(letter)] = letter
            print("\nУ вас получилось! Эта буква действительно есть в слове.")        
        else:
            print("\nИзвините, но вы не угадали.")
            guess_number += 1
            guessed_letters.append(letter)
        time.sleep(1)
        print(hangman[guess_number])
        for i in range(len(word)):
            if word[i] == letter:
                game_word[i] = letter
        print(" ".join(game_word))
        print("Угаданные буквы: " + ", ".join(guessed_letters) + "\n")
        if "_" not in game_word:
            print("Вы выиграли! Слово было "+ word.upper())
            break
        elif guess_number == 6:
            print("К сожалению, вы проиграли. Слово было " + word)
            break
    
    print("Хотите попробовать ещё раз? да/нет")
    answer = input("")
    while answer not in ["да", "нет"]:
        input("Я не могу понять, что вы ввели. Напишите, пожалуйста, ответ одним словом, да или нет: ")
    if answer.lower() == "да":
        game_rus()

answer = input("Hello and welcome to Hangman game! Please, choose the language \nЗдравствуйте и добро пожаловать в игру 'Виселица'. Пожалуйста, выберите язык:\n 1. English \n 2. Русский \n Please, type in only a number that is written near by the language's name\nПожалуйста, введите только номер, который указан возле названия языка в списке: ")

time.sleep(1)

if answer != "1" and answer != "2":
   while answer != "1" and answer != "2":
       answer = input("I can't quite understand you. Please type in only a number in the list that is written near by language's name\nЯ не могу понять, что вы ввели. Пожалуйста, введите только цифру (1 или 2): ")
if answer == "1":
    language = "eng"
if answer == "2":
    language = "rus"

if language == "eng":
    answer = input("Do you know the rules? Please type in answer in format yes|no: ")
    if answer.lower() != "yes" and answer.lower() != "no":
       while answer.lower() != "yes" and answer.lower() != "no":
        answer = input("I can't quite understand you. Please type in answer in format Yes or no: ")
    elif answer.lower() == "no":
        print("Computer chooses word randomly and you need to guess what it is one letter at a time\nThe computer draws a number of dashes equivalent to the number of letters in the word\nIf you suggest a letter that occurs in the word, the computer fills in the blanks with that letter in the right places\nIf the word does not contain the suggested letter, the computer draws one element of a hangman’s gallows\nAs the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word\nThe number of incorrect guesses before the game ends is 6\n")
    game_eng()

elif language == "rus":
    answer = input("Вы знаете правила игры? Введите ответ в формате да/нет: ")
    if answer.lower() != "да" and answer.lower() != "нет":
       while answer.lower() != "да" and answer.lower() != "нет":
        answer = input("Я не могу понять, что вы ввели. Напишите, пожалуйста, ответ одним словом, да или нет: ")
    elif answer.lower() == "нет":
        print("Компьютер выбирает слово случайным образом, и вам нужно угадывать его по букве за раз\nКомпьютер рисует количество тире, эквивалентное количеству букв в слове\ nЕсли вы предлагаете букву, которая встречается в слове, компьютер заполняет пробелы этой буквой в нужных местах\nЕсли слово не содержит предложенную букву, компьютер рисует один элемент виселицы\nПо ходу игры сегмент виселицы и жертвы добавляется каждый раз, когда вы предлагаете букву, которой нет в слове\nКоличество неправильных угадываний до конца игры - 6\n")
    game_rus()







