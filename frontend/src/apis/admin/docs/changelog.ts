import request from "@/utils/request";

type TChangelog = {
  page: number;
  pageSize: number;
};

export const getDocsChangelog = async (searchParams: TChangelog) => {
  try {
    const res = await request.get("/api/admin/docs/changelog", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getDocsChangelogById = async (id: string) => {
  try {
    const res = await request.get(`/api/admin/docs/changelog/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createDocsChangelog = async (data: any) => {
  try {
    const res = await request.post("/api/admin/docs/changelog", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateDocsChangelog = async (id: string, data: any) => {
  try {
    const res = await request.put(`/api/admin/docs/changelog/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteDocsChangelogByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/docs/changelog`, { data: { ids } });
    return res;
  } catch (error) {
    console.error(error);
  }
}
