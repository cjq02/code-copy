FILE_PATH_LIST = [
    
    # --- vue root ---  #
    'vue/package.json',
    'vue/vite.plugin.ext.js',
    'vue/vite.config.js',
    'vue/src/mixins/lib/common.mixin.js',

    # --- vue src ---  #
    'vue/src/main.js',

    # --- code ---  #
    # 'api/src/main/java/com/jiujie/{sign}/sys/service/ICodeService.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/vo/CodeVOExt.java',
    # 'api/src/main/java/com/jiujie/{sign}/application/vo/EnumVO.java',
    # 'api/src/main/java/com/jiujie/{sign}/sys/enumerate/CodeModifyStatusEnum.java',
    # 'service/src/main/resources/com/jiujie/{sign}/sys/sqlmapper/CodeMapper.xml',
    # 'service/src/main/java/com/jiujie/{sign}/sys/service/CodeService.java',
    # 'web/src/main/java/com/jiujie/{sign}/sys/web/CodeController.java',
    # 'web/src/main/java/com/jiujie/{sign}/common/web/CommonApiController.java',
    # 'web/src/main/java/com/jiujie/{sign}/sys/handler/CodeHandler.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/runner/CodeCommandLineRunner.java',
    # 'web/src/main/resources/static/template/code_js.ftl',
    # 'web/src/main/resources/static/template/code_json.ftl',
    # 'web/src/main/resources/static/template/enum_js.ftl',
    # 'web/src/main/resources/static/template/enum_class.ftl',
    # 'vue/src/api/sys/code.api.js',
    # 'vue/src/views/sys/code/codePage.js',
    # 'vue/src/views/sys/code/index.vue',
    # 'vue/src/views/sys/code/components/CodeForm/codeForm.js',
    # 'vue/src/views/sys/code/components/CodeForm/index.vue',
    # 'vue/src/views/sys/code/components/CompareForm/compareForm.js',
    # 'vue/src/views/sys/code/components/CompareForm/index.vue',
    # 'vue/src/views/sys/code/components/GenerateEnumDialog/index.vue',
    # 'vue/src/views/sys/code/components/ButtonEnumPackage/index.vue',
    # 'vue/src/views/sys/code/components/ButtonEnumPackage/index.scss',
    
    # --- application ---  #
    # 'api/src/main/java/com/jiujie/{sign}/application/vo/Page.java',
    
    # --- components ---  #
    # 'vue/src/components/TableComb/index.vue',
    # 'vue/src/components/TableEdit/index.vue',
    'vue/src/components',
    
    # --- layout ---  #
    # 'vue/src/layout/components/Navbar.vue',
    # 'vue/src/layout/components/Sidebar/index.vue',
    'vue/src/layout/components/TagsView/TagsView.vue',
    
    # --- mixin ---  #
    # 'vue/src/mixin/dragTable.mixin.js',
    # 'vue/src/mixin/codeMap.mixin.js',
    # 'vue/src/mixin/permission.mixin.js',
    
    # --- styles ---  #
    'vue/src/styles/common.scss',
    'vue/src/styles/sidebar.scss',
    
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

    # --- mybatis ---  #
    # 'service/src/main/resources/META-INF/mybatis/mybatis-config.xml',
    # 'service/src/main/java/com/jiujie/{sign}/application/mybatis/SortInterceptor.java',

    # --- shiro ---  #
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/BaseFormAuthenticationFilter.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/WebRealm.java',
    # 'web/src/main/java/com/jiujie/{sign}/application/shiro/SimpleCaptchaServlet.java',
    
    # --- business ---  #
    # 'vue/src/views/sys/user/index.vue',
    # 'vue/src/views/sys/corp/index.vue',
    # 'vue/src/views/sys/role/index.vue',
    # 'vue/src/views/sys/corp/index.vue',
    # 'vue/src/views/sys/user/user.js',
    # 'vue/src/views/sys/menu/menu.js',
    # 'vue/src/views/sys/role/role.js',
    # 'vue/src/views/sys/corp/corp.js',
    # 'vue/src/api/sys/menu.api.js',
    # 'vue/src/api/sys/role.api.js',
    # 'vue/src/api/sys/user.api.js',
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









