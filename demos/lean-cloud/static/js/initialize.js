var KEY = '9sjs3qnjnj9ph8a8srt9py6ign4ggluqkqyfwxmwfznt7bpr',
		SECRET = '010ifb5frusffez9yolal3vt50forlpi1sd9d92g699k541i';

AV.initialize(KEY, SECRET);

var NoteDraft = AV.Object.extend('NoteDraft'),
		queryNoteDraft = new AV.Query(NoteDraft);