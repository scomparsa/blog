queryNoteDraft.get(OBJECT_ID, {
	success: function(result) {
		// parse JSON
		var jsonStr = result.get('json'),
				jsonObj = JSON.parse(jsonStr),
				createdAt = new Date(parseInt(jsonObj.mCreateTime*1000)).toLocaleString(),
				fontName = jsonObj.mFontName,
				fontSize = jsonObj.mFontSize,
				bgId = jsonObj.mSelectBgId,
				textHeight = jsonObj.mTextHeight,
				noteItems = jsonObj.mNoteItems;

		var headerImg = '/static/img/0'+bgId+'/head@2x.png',
				bodyBg = 'url(/static/img/0'+bgId+'/body@2x.png)',
				footerImg = '/static/img/0'+bgId+'/foot@2x.png',
				$header = $('header'),
				$body = $('.ui-body'),
				$footer = $('footer');

		// render header
		$header.prepend('<img class="img-responsive" src="'+headerImg+'">')
					 .find('h4').html(createdAt);

		// render body
		$body.css({ 'background-image': bodyBg });
		_.each(noteItems, function(noteItem) {
				var content = noteItem.content,
						remoteUrl = noteItem.mRemoteUrl;

				if (remoteUrl && remoteUrl != '<null>') {
					$body.append('<img class="img-responsive" src="'+remoteUrl+'"><br><br>');
				} else {
					if (content && content != '<null>') {
						$body.append(content+'<br><br>');
					}
				}
		});

		// render footer
		$footer.html('<img class="img-responsive" src="'+footerImg+'">');
	},
	error: function(err) {
		console.dir(err);
	}
});