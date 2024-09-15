import request from "@/utils/request";

type TBlogCategory = {
  page: number;
  pageSize: number;
  categoryId?: number;
  tagId?: number;
};

export const getBlog = async (searchParams: TBlogCategory) => {
  try {
    const res = await request.get("/api/admin/blog/", {
      params: {
        page: searchParams.page,
        pageSize: searchParams.pageSize,
        categoryId: searchParams.categoryId,
        tagId: searchParams.tagId,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
