import { NewsContent } from '@/components/Client/NewsDetail/news-content';
import { NewsHeader } from '@/components/Client/NewsDetail/news-header';
import { createFileRoute } from '@tanstack/react-router'
import { getNewsById } from '@/apis/client/news';

export const Route = createFileRoute('/_client/news/$id')({
  component: NewsDetailRoute,
  async loader({ params }) {
    const result: any = await getNewsById(Number(params.id))
    if(result && result.code === 0) {
      return result.data
    }
  }
})

export function NewsDetailRoute() {
  const news = Route.useLoaderData();
  return (
    <div className="flex flex-col pt-[140px] w-[40vw] h-[80vh]">
      <NewsHeader news={news} />
      <NewsContent content={news.content} />
    </div>
  );
}
