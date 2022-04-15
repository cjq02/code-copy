FILE_PATH_LIST = [

    # --- vue root ---  #
    'vue/package.json',
    'vue/vite.plugin.ext.js',
    'vue/vite.config.js',
    'vue/.eslintrc.js',

    # --- vue src ---  #
    'vue/src/main.ts',
    'vue/src/common/global.ts',

    # --- code ---  #
    'api/src/main/java/com/jiujie/{sign}/sys/service/ICodeService.java',
    'api/src/main/java/com/jiujie/{sign}/sys/vo/CodeVOExt.java',
    'api/src/main/java/com/jiujie/{sign}/application/vo/EnumVO.java',
    'api/src/main/java/com/jiujie/{sign}/sys/enumerate/CodeModifyStatusEnum.java',
    'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/CodeMapper.xml',
    'service/src/main/java/com/jiujie/{sign}/sys/service/CodeService.java',
    'web/src/main/java/com/jiujie/{sign}/sys/web/CodeController.java',
    # 'web/src/main/java/com/jiujie/{sign}/common/web/CommonApiController.java',
    'web/src/main/java/com/jiujie/{sign}/sys/handler/CodeHandler.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/runner/CodeCommandLineRunner.java',
    'web/src/main/resources/static/template/code_js.ftl',
    'web/src/main/resources/static/template/code_json.ftl',
    'web/src/main/resources/static/template/enum_js.ftl',
    'web/src/main/resources/static/template/enum_class.ftl',
    'vue/src/api/sys/code.api.js',
    'vue/src/views/sys/code',

    # --- api ---  #
    'vue/src/api/common.api.js',
    # 'vue/src/api/sys/menu.api.js',
    # 'vue/src/api/sys/role.api.js',
    # 'vue/src/api/sys/user.api.js',

    # --- components ---  #
    # 'vue/src/components/TableComb/index.vue',
    # 'vue/src/components/TableEdit/index.vue',
    'vue/src/components',

    # --- filters ---  #
    'vue/src/filters',

    # --- hooks ---  #
    'vue/src/hooks',

    # --- layout ---  #
    # 'vue/src/layout/components/Navbar.vue',
    # 'vue/src/layout/components/Sidebar/index.vue',
    # 'vue/src/layout/components',
    'vue/src/layout/components/ResetPwd/index.vue',

    # --- mixin ---  #
    # 'vue/src/mixins/lib/common.mixin.js',
    'vue/src/mixins',

    # --- store ---  #
    'vue/src/store',

    # --- styles ---  #
    'vue/src/styles',
    # 'vue/src/styles/common.scss',
    # 'vue/src/styles/sidebar.scss',

    # --- views/sys ---  #
    # 'vue/src/views'
    # 'vue/src/views/sys/code',
    'vue/src/views/account',
    'vue/src/views/sys',

    # --- iconfont ---  #
    # 'vue/src/styles/font/demo.css',
    # 'vue/src/styles/font/demo_index.html',
    # 'vue/src/styles/font/iconfont.css',
    # 'vue/src/styles/font/iconfont.js',
    # 'vue/src/styles/font/iconfont.json',
    # 'vue/src/styles/font/iconfont.ttf',
    # 'vue/src/styles/font/iconfont.woff',
    # 'vue/src/styles/font/iconfont.woff2',

    # --- utils ---  #
    # 'vue/src/utils/request.js',
    # 'vue/src/utils/excel.utils.js',
    # 'vue/src/utils',

    # --- application ---  #
    # 'api/src/main/java/com/jiujie/{sign}/application/vo/Page.java',

    # --- mybatis ---  #
    # 'service/src/main/resources/META-INF/mybatis/mybatis-config.xml',
    # 'service/src/main/java/com/jiujie/{sign}/application/mybatis/SortInterceptor.java',

    # --- shiro ---  #
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/BaseFormAuthenticationFilter.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/WebRealm.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/SimpleCaptchaServlet.java',

    # --- business ---  #
    'web/src/main/java/com/jiujie/{sign}/sys',
    'service/src/main/java/com/jiujie/{sign}/sys',
    'api/src/main/java/com/jiujie/{sign}/sys',
    'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper',
    # 'vue/src/views/sys/user/index.vue',
    # 'vue/src/views/sys/corp/index.vue',
    # 'vue/src/views/sys/role/index.vue',
    # 'vue/src/views/sys/corp/index.vue',
    # 'vue/src/views/sys/user/user.js',
    # 'vue/src/views/sys/menu/menu.js',
    # 'vue/src/views/sys/role/role.js',
    # 'vue/src/views/sys/corp/corp.js',
    # 'vue/src/store/modules/menu.module.js',
    # 'web/src/main/java/com/jiujie/{sign}/sys/web/MenuController.java',
    # 'web/src/main/java/com/jiujie/{sign}/sys/web/RoleController.java',
    # 'web/src/main/java/com/jiujie/{sign}/sys/web/UserController.java',
    # 'web/src/main/java/com/jiujie/{sign}/sys/web/CorpController.java',
    # 'service/src/main/java/com/jiujie/{sign}/sys/service/MenuService.java',
    # 'service/src/main/java/com/jiujie/{sign}/sys/service/RoleService.java',
    # 'service/src/main/java/com/jiujie/{sign}/sys/service/UserService.java',
    # 'service/src/main/java/com/jiujie/{sign}/sys/service/CorpService.java',
    # 'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/MenuMapper.xml',
    # 'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/RoleMapper.xml',
    # 'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/UserMapper.xml',
    # 'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/CorpMapper.xml',
    # 'api/src/main/java/com/jiujie/{sign}/sys/service/IMenuService.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/service/IRoleService.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/service/IUserService.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/service/ICorpService.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/vo/UserVOExt.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/web/LoginController.java'
]


def get_file_path_list():
    return FILE_PATH_LIST
