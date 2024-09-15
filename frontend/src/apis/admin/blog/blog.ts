import request from "@/utils/request";

type TBlogCategory = {
  page: number;
  pageSize: number;
  categoryName?: string;
  tagName?: string;
}

export const getBlogCategory = async (searchParams : TBlogCategory) => {
  try {
    const res = await request.get("/api/admin/blog/category", {
      params: { page: searchParams.page, size: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
