import { ButtonLink } from "@/components/common/button-link";

export const createBlogCategoryToolBarRender = () => {
  return [
    <ButtonLink
      key="tag-modal"
      to={`/admin/blog/edit`}
      type={"new"}
      content="新建"
    />,
  ];
};
