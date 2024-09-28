import request from "@/utils/request";

type TBlogTag = {
  page: number;
  pageSize: number;
};

export const getBlogTag = async (searchParams: TBlogTag) => {
  try {
    const res = await request.get("/api/admin/blog/tag/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getBlogTagById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/blog/tag/${id}`);
    return res
  } catch (error) {
    console.error(error);
  }
}

export const createBlogTag = async (data: any) => {
  try {
    const res = await request.post("/api/admin/blog/tag/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateBlogTagById = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/blog/tag/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteBlogTagByIds = async (ids: number)  => {
  try {
    const res = await request.delete("/api/admin/blog/tag/", {
      data: { ids },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
