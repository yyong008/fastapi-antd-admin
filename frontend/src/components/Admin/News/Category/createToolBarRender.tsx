import { NewsCategoryModalCreate } from "./NewsCategoryModalCreate";

export const createToolBarRender =
  ({ refetch }) =>
  () => [
    <NewsCategoryModalCreate
      key="news-category-modal-create"
      refetch={refetch}
    />,
  ];
