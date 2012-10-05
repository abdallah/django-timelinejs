dojo.require("dijit.Editor");

// extra plugins
dojo.require("dijit._editor.plugins.FontChoice");
dojo.require("dojox.editor.plugins.TextColor");
dojo.require("dojox.editor.plugins.Blockquote");
dojo.require("dijit._editor.plugins.LinkDialog");
dojo.require("dojox.editor.plugins.InsertAnchor");
dojo.require("dojox.editor.plugins.FindReplace");
dojo.require("dojox.editor.plugins.ShowBlockNodes");
dojo.require("dojox.editor.plugins.PasteFromWord");
dojo.require("dijit._editor.plugins.ViewSource");
dojo.require("dijit._editor.plugins.FullScreen");
dojo.require("dojox.editor.plugins.InsertEntity");

// headless plugins
dojo.require("dojox.editor.plugins.CollapsibleToolbar");
dojo.require("dojox.editor.plugins.NormalizeIndentOutdent");
dojo.require("dojox.editor.plugins.PrettyPrint");	// let's pretty-print our HTML
dojo.require("dojox.editor.plugins.AutoUrlLink");
dojo.require("dojox.editor.plugins.ToolbarLineBreak");

dojo.ready(function(){
  var textareas = dojo.query("textarea");
  if(textareas && textareas.length){
    dojo.addClass(dojo.body(), "claro");
    textareas.instantiate(dijit.Editor, {
      //styleSheets: "/appmedia/style.css;/appmedia/blog/style.css",
      plugins: [
        "collapsibletoolbar",
        "fullscreen", "viewsource", "|",
        "undo", "redo", "|",
        "cut", "copy", "paste", "|",
        "bold", "italic", "underline", "strikethrough", "|",
        "insertOrderedList", "insertUnorderedList", "indent", "outdent", "||",
        "formatBlock", "fontName", "fontSize", "||",
        "findreplace", "insertEntity", "blockquote", "|",
        "createLink", "insertImage", "insertanchor", "|",
        "foreColor", "hiliteColor", "|",
        "showblocknodes", "pastefromword",
        // headless plugins
        "normalizeindentoutdent", "prettyprint",
        "autourllink", "dijit._editor.plugins.EnterKeyHandling"
      ]
    });
  }
});