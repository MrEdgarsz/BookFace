$(function () {
    // init TinyMCE editors
    tinymce.init({
        selector: '#postForm',
        language: 'pl',
        resize: false,
        toolbar_mode: 'floating',
        plugins: [
            'lists','link','image','charmap','preview','searchreplace','visualblocks',
            'insertdatetime','media','help','wordcount'
        ],
        init_instance_callback: (editor) => {
            console.log(`Editor: ${editor.id} is now initialized.`);
        },
        setup: function (editor) {
            editor.on('input', function () {
                tinymce.triggerSave();
                checkPostForm();
            });
        }
    });

    tinymce.init({
        selector: '.editPostForm',
        language: 'pl',
        resize: false,
        toolbar_mode: 'floating',
        plugins: [
            'lists','link','image','charmap','preview','searchreplace','visualblocks',
            'insertdatetime','media','help','wordcount'
        ],
        init_instance_callback: (editor) => {
            console.log(`Editor: ${editor.id} is now initialized.`);
        },
        setup: function (editor) {
            editor.on('input', function () {
                tinymce.triggerSave();
                var content = tinymce.activeEditor.getContent();
                checkEditPostForm(editor.id, content);
            });
        }
    });

    // prevent Bootstrap modal dialog from blocking focusin
    document.addEventListener('focusin', (e) => {
        if (e.target.closest('.tox-tinymce-aux, .moxman-window, .tam-assetmanager-root') !== null) {
            e.stopImmediatePropagation();
        }
    });
});

function checkPostForm() {
    var editorContent = $('#postForm').val();
    var editorContentInText = $.trim($(editorContent).text());

    if (editorContentInText == '') {
        return $('#postFormSubmit').prop('disabled', true);
    }

    $('#postFormSubmit').prop('disabled', false);
}

function checkEditPostModal(postId) {
    checkEditPostForm(postId);
    setPostDefaultValue(postId);
}

function setPostDefaultValue(postId) {
    const editPost = document.getElementById('editPost-' + postId);
    editPost.addEventListener('show.bs.modal', event => {
        const button = event.relatedTarget;
        const postContent = button.getAttribute('data-bs-defaultvalue');
        tinymce.activeEditor.setContent(postContent);
    })
    editPost.addEventListener('hide.bs.modal', event => {
        const button = event.relatedTarget;
        const postContent = button.getAttribute('data-bs-defaultvalue');
        tinymce.activeEditor.setContent(postContent);
    })
}

function checkEditPostForm(postId, postDesc) {
    var editorContent = $('#' + postId).val();
    var editorContentInText = $.trim($(editorContent).text());
    var submitBtn = postId + '-Submit';
		
    if (editorContentInText == '' || editorContentInText == postDesc) {
        return $('#' + submitBtn).prop('disabled', true);
    }
        
    $('#' + submitBtn).prop('disabled', false);
}