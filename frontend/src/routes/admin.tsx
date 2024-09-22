import { Outlet, createFileRoute, redirect } from "@tanstack/react-router";
import { ProLayout, WaterMark } from "@ant-design/pro-components";
import { memo, useContext, useMemo, useState } from "react";

import { AvatarDropDown } from "@/components/Layout/Admin/avatar-dropdown";
import { Footer } from "@/components/common/footer";
import { MenuFooterRender } from "@/components/Layout/Admin/menu-footer-render";
import { MenuItemLink } from "@/components/common/menu-item-link";
import { MenuItemOutLink } from "@/components/common/menu-item-outer-link";
import { SettingContext } from "@/context";
import { SettingDrawerWrap } from "@/components/Layout/Admin/setting-drawer-wrap";
import { createActionRenderWrap } from "@/components/Layout/Admin/create-actions-render";
import { createProLayoutRoute } from "@/utils/create-prolayout-route";
import { createTokens } from "@/components/Layout/Admin/create-token";
import { getLocalStorageToken } from "@/utils/localstorage";
import { getUserInfo } from "@/apis/userinfo";
import { prolayoutConfig } from "@/config/prolayout";

export const Route = createFileRoute("/admin")({
  beforeLoad(){
    if(!getLocalStorageToken()) {
      throw redirect({ to: "/admin/login"});
    }
  },
  async loader() {
    const res: any = await getUserInfo();
    if(res && res.code === 0) {
      localStorage.setItem('userInfo', JSON.stringify(res.data.userInfo))
    } else {
      throw redirect({ to: "/admin/login"});
    }
    return res?.data;
  },
  component: memo(AdminComponent),
});

const resetStyles = {
  padding: "0px",
  margin: "0px",
  height: "100vh",
};

function AdminComponent() {
  const value = useContext(SettingContext);
  const data = Route.useLoaderData();
  const {userInfo = {}, menu = []} = data || {}
  const [pathname, setPathname] = useState(location.pathname);
  const token = useMemo(() => createTokens(value), [value]);

  const route = useMemo(() => createProLayoutRoute(menu), [menu]);

  return (
    <WaterMark content="FastAPI Antd Admin">
      <ProLayout
        location={{
          pathname,
        }}
        route={route}
        token={token}
        // loading={isLoading}
        {...value.theme}
        logo={prolayoutConfig.logo}
        menu={prolayoutConfig.menu}
        style={resetStyles}
        title={prolayoutConfig.title}
        ErrorBoundary={false}
        pageTitleRender={false}
        contentStyle={resetStyles}
        layout={prolayoutConfig.layout as any}
        footerRender={() => <Footer />}
        suppressSiderWhenMenuEmpty={true}
        menuFooterRender={MenuFooterRender}
        actionsRender={createActionRenderWrap({ value })}
        avatarProps={{
          src: userInfo?.avatar || prolayoutConfig.avatar.src,
          size: prolayoutConfig.avatar.size as any,
          title: userInfo?.name,
          render: (_, dom) => {
            return <AvatarDropDown dom={dom} />;
          },
        }}
        menuItemRender={(item, dom) => {
          if (item.isLink) {
            return <MenuItemOutLink path={item.path!} dom={dom} />;
          }

          return (
            <MenuItemLink
              path={item.path!}
              dom={dom}
              setPathname={setPathname}
            />
          );
        }}
      >
        <Outlet />
        <SettingDrawerWrap theme={value.theme} setTheme={value.setTheme} />
      </ProLayout>
    </WaterMark>
  );
}
