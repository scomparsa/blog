queryNoteDraft.find({
	success: function(results) {
		// parse objectId
		var objectIds = [];
		_.each(results, function(result) {
			objectIds.push(result.id);
		});

		// render DOM
		var html = [];
		html.push('<table class="table table-bordered table-stripped"><thead class="well"><tr><th>Object ID</th></tr></thead><tbody>');
		_.each(objectIds, function(objectId) {
			html.push('<tr><td><a href="/note_drafts/'+objectId+'" target="_blank">'+objectId+'</a></td></tr>');
		});
		html.push('</tbody></table>');

		$('#data').html(html.join(''));
	},
	error: function(err) {
		console.dir(err);
	}
});