const aws = require('aws-sdk');
const s3 = new aws.S3({apiVersion: '2006-03-01'});
const axios = require('axios');

exports.uploadSitemap = async (event, context, callback) => {
  const message = JSON.parse(event.Records[0].Sns.Message);
  const url = message.url;
  const bucket = message.bucket;

  if (!url || !bucket) {
    callback('must have url and bucket argument');
  }

  const request = await axios.get(url);
  await s3.putObject({
    Bucket: bucket,
    Key: 'sitemap.xml',
    Body: request.data,
    ACL: 'public-read',
    // no cache so we do not have to invalidate cloudfront
    CacheControl: 'no-cache',
  }).promise();
  await axios.get('https://ww.google.com/webmasters/tools/ping?sitemap=https://' + bucket + '/sitemap.xml');
  return callback(null, 'success');
};

exports.setCache = async (event, context, callback) => {
  const message = JSON.parse(event.Records[0].Sns.Message);
  const url = message.url;
  if (!url) {
    callback('url required');
  }

  await axios.post('https://api.prerender.io/recache', {
    prerenderToken: process.env.PRERENDER_TOKEN,
    url: url,
  });
  const lastLetterOfUrl = url.slice(-1);
  let secondaryUrl;
  if (lastLetterOfUrl === '/') {
    secondaryUrl = url.slice(0, -1);
  } else {
    secondaryUrl = url + '/';
  }
  await axios.post('https://api.prerender.io/recache', {
    prerenderToken: process.env.PRERENDER_TOKEN,
    url: secondaryUrl,
  });
  callback(null, 'success');
}
