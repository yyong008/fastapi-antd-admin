import { ButtonLink } from "@/components/common/button-link";

export const createToolBarRender = () => () => [
  <ButtonLink
    key="create-news-modal"
    type="new"
    content="添加新闻"
    to={`/admin/news/edit`}
  />,
];
