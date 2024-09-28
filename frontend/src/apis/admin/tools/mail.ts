import request from "@/utils/request";

type TMail = {
  page: number;
  pageSize: number;
};

export const getToolsMail = async (searchParams: TMail) => {
  try {
    const res = await request.get("/api/admin/tools/mail/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getMailById = async (id: string) => {
  try {
    const res = await request.get(`/api/admin/tools/mail/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createMail = async (data: any) => {
  try {
    const res = await request.post("/api/admin/tools/mail/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateMailById = async (id: string, data: any) => {
  try {
    const res = await request.put(`/api/admin/tools/mail/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteMailByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/tools/mail/`, {
      data: { ids: ids },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
