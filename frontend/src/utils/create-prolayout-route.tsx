import { AntdIcon } from "@/components/common/antd-icon";
import { isExternalLink } from "./utils";

function createProLayoutRouteImpl(
  items: any[],
  parentId: number | null,
): any[] {
  return items
    .filter((item) => item.parent_menu_id === parentId)
    .map((item) => ({
      ...item,
      name: item.name,
      path: isExternalLink(item.path)
        ? item.path
        : `/admin${item.path}`,
      key: item.id + item.path, // https://github.com/ant-design/pro-components/issues/2511
      hideInMenu: !item.isShow,
      icon: item.icon ? <AntdIcon name={item.icon} /> : item.icon,
      children: createProLayoutRouteImpl(items, item.id), // 递归构建子树
    }))
    .sort((a, b) => a.order_no - b.order_no);
}

/**
 * 创建 prolayout 的路由列表（加入 TSX icon）
 * @param menus 传入字符串 icon 菜单
 * @returns
 */
export const createProLayoutRoute = (menus: any): any => {
  return {
    routes: createProLayoutRouteImpl(menus, null),
  };
};
