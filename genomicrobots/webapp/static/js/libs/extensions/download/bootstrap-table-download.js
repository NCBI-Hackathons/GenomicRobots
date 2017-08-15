/**
 * @author Alexander Goncearenco
 */

(function ($) {
    'use strict';
    var sprintf = $.fn.bootstrapTable.utils.sprintf;

    $.extend($.fn.bootstrapTable.defaults, {
        showDownload: false,
        downloadTypes: ['TXT']
    });

    $.extend($.fn.bootstrapTable.defaults.icons, {
        download_data: 'glyphicon-export icon-share'
    });

    var BootstrapTable = $.fn.bootstrapTable.Constructor,
        _initToolbar = BootstrapTable.prototype.initToolbar;

    BootstrapTable.prototype.initToolbar = function () {
        if (!this.showToolbar) {
            this.showToolbar = this.options.showDownload;
        }

        _initToolbar.apply(this, Array.prototype.slice.apply(arguments));

        if (this.options.showDownload) {

            var that = this,
                $btnGroup = this.$toolbar.find('>.btn-group'),
                $download = $btnGroup.find('div.download');

            if (!$download.length) {
                $download = $([
                    '<div class="download btn-group">',
                        '<button class="btn btn-default' +
                            sprintf(' btn-%s', this.options.iconSize) +
                            ' dropdown-toggle" ' +
                            'data-toggle="dropdown" type="button">',
                            sprintf('<i class="%s %s"></i> ', this.options.iconsPrefix, this.options.icons.download_data),
                            '<span class="caret"></span>',
                        '</button>',
                        '<ul class="dropdown-menu" role="menu">',
                        '</ul>',
                    '</div>'].join('')).appendTo($btnGroup);

                var $menu = $download.find('.dropdown-menu'),
                    downloadTypes = this.options.downloadTypes;

                if (typeof this.options.downloadTypes === 'string') {
                    var types = this.options.downloadTypes.slice(1, -1).replace(/ /g, '').split(',');

                    downloadTypes = [];
                    $.each(types, function (i, value) {
                        downloadTypes.push(value.slice(1, -1));
                    });
                }
                $.each(downloadTypes, function (i, type) {
                        $menu.append(['<li data-type="' + type + '">',
                                '<a href="javascript:void(0)">',
                                    type,
                                '</a>',
                            '</li>'].join(''));
                });

                $menu.find('li').click(function () {
                    var type = $(this).data('type');
            	    // console.log(that.options.url);
            	    // console.log(window[that.options.queryParams]({format: 'txt'}));
            	    window.location.href = that.options.url + "?" + $.param(window[that.options.queryParams]({format: type}));
                });
            }
        }
    };
})(jQuery);
