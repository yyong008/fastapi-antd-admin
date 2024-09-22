import request from "@/utils/request";

type TBlogCategory = {
  page: number;
  pageSize: number;
};

export const getBlogCategory = async (searchParams: TBlogCategory) => {
  try {
    const res = await request.get("/api/admin/blog/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getBlogById = async (id: number) => {
  try {
    const res = await request.get("/api/admin/blog/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
};
